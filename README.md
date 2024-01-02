# Web Scraping and Temperature Data Visualization

This repository is dedicated to a unique integration of web scraping and data visualization, focusing on the extraction and graphical representation of temperature data from diverse online sources. It showcases the capability to collect real-time data and transform it into engaging, interactive visualizations.

## 🚀 Overview

The project is a testament to the power of combining data extraction from the web with sophisticated visualization techniques, primarily aimed at temperature data. It is an excellent resource for those interested in learning about web scraping and the dynamic presentation of data.

## 📋 Project Components

### Prerequisites

- Basic knowledge of Python programming.

- Familiarity with data visualization libraries like Matplotlib.

- Understanding of web scraping concepts.

### 🛠 Installation & Operation Guide

1. **Setting Up the Environment:**
    Ensure Python is installed and then set up a virtual environment:
    ```
    python -m venv .venv
    source .venv/bin/activate  # On Linux/MacOS
    .venv\Scripts\activate  # On Windows
    ```

2. **Dependency Installation:**
    Install necessary Python libraries:
    ```
    pip install playwright pandas matplotlib h5py
    ```

3. **Web Scraping for Temperature Data:**

- Run the `scraper.py` script to scrape temperature data from listed websites.

- Data is extracted using Playwright and stored in an HDF5 file (`weather_data.hd5`).

4. **Data Visualization with Matplotlib:**

- Execute `visualisation.py` to read the HDF5 file and visualize the data.

- Temperature trends are plotted using dynamic line charts, featuring timestamps on the x-axis and temperature values on the y-axis.

5. **Understanding the Output:**

- The resulting plot (`temperature_plot.pdf`) displays temperature trends from various sources, aiding in comparative analysis.

6. **Customization and Exploration:**

- Users can add or modify URLs in the websites.csv file for scraping additional data sources.

- Explore different visualization techniques by modifying the visualisation.py script.

> Note: For Unix systems, replace python with python3 in the command line instructions.