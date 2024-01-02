import h5py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_FILENAME = 'weather_data.hd5'

if __name__ == '__main__':
    with h5py.File(DATA_FILENAME, 'r') as file:
        euronews_timestamp = np.array(file.get(
            'www.euronews.com/timestamp'
        )).astype('datetime64', copy=False)
        euronews_temperature = np.array(file.get(
            'www.euronews.com/temperature'
        ))
        topweather_timestamp = np.array(file.get(
            'www.topweather.net/timestamp'
        )).astype('datetime64', copy=False)
        topweather_temperature = np.array(file.get(
            'www.topweather.net/temperature'
        ))
        meteostat_timestamp = np.array(file.get(
            'meteostat.net/timestamp'
        )).astype('datetime64', copy=False)
        meteostat_temperature = np.array(file.get(
            'meteostat.net/temperature'
        ))

        euronews = pd.DataFrame({
            'timestamp': euronews_timestamp,
            'temperature': euronews_temperature,
            'website': 'euronews.com'
        })
        topweather = pd.DataFrame({
            'timestamp': topweather_timestamp,
            'temperature': topweather_temperature,
            'website': 'topweather.net'
        })
        meteostat = pd.DataFrame({
            'timestamp': meteostat_timestamp,
            'temperature': meteostat_temperature,
            'website': 'meteostat.net'
        })

    data = pd.concat([euronews, topweather, meteostat], axis=0)

    fig, ax = plt.subplots()
    for website in data['website'].unique():
        website_data = data[data['website'] == website]
        ax.plot(
            website_data['timestamp'],
            website_data['temperature'],
            label=website
        )

    combined_time = data['timestamp'].unique()
    combined_time = pd.to_datetime(combined_time).sort_values()

    tick_dates = combined_time[::24]
    tick_labels = [date.strftime('%Y-%m-%d') for date in tick_dates]

    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Temperature (°C)')
    ax.set_xticks(tick_dates)
    ax.set_xticklabels(tick_labels, rotation=45, ha='right')
    ax.legend()

    fig.savefig('temperature_plot.pdf', format='pdf', bbox_inches='tight')