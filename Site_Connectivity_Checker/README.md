# 🌐 Website Connectivity Checker
This is a simple and efficient web application built with Streamlit that allows users to check the connectivity status of multiple websites. It uses Python’s `requests` library to perform HTTP GET requests and displays whether each site is up, down, or unreachable.

## Features

- Check multiple URLs at once

- Automatically formats and standardizes input URLs

- Fast and responsive using multi-threading (`concurrent.futures`)

- Simple and clean UI built with Streamlit

- Copy-paste multiple URLs (one per line)


## How It Works
Input URLs: The user enters one or more URLs (one per line) into a text area.

Format URLs: The app formats all input to ensure consistency, adding the `https://www.` prefix if missing.

Connectivity Check: For each formatted URL, the app sends an HTTP GET request using a browser-like user-agent string.

Multithreading: Uses Python’s `ThreadPoolExecutor` to check all websites in parallel.

Results Displayed: The status of each site is shown as:

✅ Website is up (status code 200)

⚠️ Website is down (non-200 status)

❌ Website unreachable (network error or timeout)

## Project Structure
```bash
site-connectivity-checker/
│
├── src/
│   ├─site_connectivity_checker_Dashboard.py
│   └──site_connectivity_checker.py
│ 
├── requirements.txt
└── README.md

```

## Installation
1. Install dependencies
It's recommended to use a virtual environment:
```bash
pip install -r requirements.txt
```
2. Run the app
```bash
streamlit run app.py
```

## Example
**Input:**
```bash
https://www.google.com
https://www.example.com/notfoundpage
https://www.github.com
https://www.stackoverflow.co
https://www.python.org
https://nonexistentwebsite.example
```
**Output:**
```bash
✅ https://www.google.com is up!

⚠️ https://www.example.com/notfoundpage is down. Status Code: 404

✅ https://www.github.com is up!

✅ https://www.stackoverflow.co is up!

✅ https://www.python.org is up!

❌ Failed to reach https://www.nonexistentwebsite.example. Error: HTTPSConnectionPool(host='www.nonexistentwebsite.example', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x0000019F8AC80E10>: Failed to resolve 'www.nonexistentwebsite.example' ([Errno 11001] getaddrinfo failed)"))
```
## Notes
- Only basic URL validation is done; the app assumes user input is correct after formatting.

- This tool is not a comprehensive uptime monitor — it's for quick checks only.
---
<p align="center">👧 Author: <b>Mina Jazini</b></p>