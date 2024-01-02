from datetime import datetime

import h5py
import numpy as np
import pandas as pd
from playwright.sync_api import sync_playwright

INPUT_FILENAME = 'websites.csv'
OUTPUT_FILENAME = 'weather_data.hd5'

if __name__ == '__main__':
    df = pd.read_csv(INPUT_FILENAME)
    urls = df['url']

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        for index, url in enumerate(urls):
            page.goto(url)

            if index == 0:
                page.locator('css=#didomi-notice-agree-button').click()
                value = page.locator(
                    'css=span.c-current-weather__temperature.unit_C.ltr'
                ).inner_text()
                value = value.replace('°C', '')
                value = value.strip()
            elif index == 1:
                value = page.locator('css=div.degree-in').inner_text()
                value = value.replace('°C', '')
            else:
                value = page.get_by_role('heading', name='°C').inner_text()
                value = value.replace('°C', '')
                value = value.strip()

            value = np.array([value]).astype(float)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with h5py.File(OUTPUT_FILENAME, 'a') as file:
                group_name = url.split('//')[-1].split('/')[0]
                if group_name in file:
                    group = file[group_name]
                else:
                    group = file.create_group(group_name)

                if 'temperature' in group:
                    temperature_dataset = group['temperature']
                    temperature_dataset.resize(
                        temperature_dataset.shape[0] + 1,
                        axis=0
                    )
                    temperature_dataset[-1] = value
                else:
                    temperature_dataset = group.create_dataset(
                        'temperature',
                        shape=(1,),
                        maxshape=(None,),
                        chunks=True,
                        dtype=float
                    )
                    temperature_dataset[0] = value

                if 'timestamp' in group:
                    timestamp_dataset = group['timestamp']
                    timestamp_dataset.resize(
                        timestamp_dataset.shape[0] + 1,
                        axis=0
                    )
                    timestamp_dataset[-1] = np.string_(timestamp)
                else:
                    timestamp_dataset = group.create_dataset(
                        'timestamp',
                        shape=(1,),
                        maxshape=(None,),
                        dtype=h5py.special_dtype(vlen=str)
                    )
                    timestamp_dataset[0] = np.string_(timestamp)

        browser.close()
