# 🌍 Country Info Dashboard

A simple and interactive Streamlit web application to retrieve and display detailed information about any country using the [REST Countries API](https://restcountries.com/).

## 📌 Features

- 🔍 Search and select any country from a dropdown menu.
- 📊 View detailed information:
  - Capital
  - Region
  - Population
  - Official Languages
  - Currencies (with names and symbols)
  - National Flag


## Project Structure
```bash
Country_info/
│
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── src/
│ ├── country_info.py # Function to fetch and return country info
│ └── country_info_dashboard.py # Streamlit dashboard app
```

## Run the App

Make sure you have Python 3.7 or later installed.
```bash
pip install -r requirements.txt
```

From the `src` directory:
```bash
streamlit run country_info_dashboard.py
```
## How It Works
- The file country_info.py defines a function county_info() that:

    - Sends a GET request to the REST Countries API.

    - Extracts key country data (capital, region, languages, population, currencies, flag).

    - Returns the data in a dictionary format.

- The file country_info_dashboard.py:

    - Builds a dashboard UI with Streamlit.

    - Lets the user select a country from a dropdown.

    - Displays country data in a formatted HTML table, including the national flag.

## Sample Output
You can expect an output like the image below when running the app:
```
Flag and country info shown in a table format
```

---
<p align="center">👧 Author: <b>Mina Jazini</b></p>