# Password Generator Dashboard

## Project Overview
The **Password Generator Dashboard** is an interactive web application built with Python and Streamlit.  
It enables users to quickly generate different types of passwords based on their preferences:  
- **Random Passwords** with customizable length  
- **PIN Codes** consisting of numbers only  
- **Memorable Passwords** designed to be easier to remember  

The app provides a clean and simple interface for effortless password creation.


## Project Structure
```Generate Password/
└── Dashboard of project/
    ├── images/
    │   └── streamlit-dashboard.png  
    ├── src/ 
    │   ├── Password_Dashboard.py
    │   └── Password_Generatore.py
    ├── README.md
    └── requirement.txt
```

## Getting Started

Follow the instructions below to set up this project on your local machine.

### Prerequisites

- Python 3.6 or later
- Streamlit
- NLTK (Natural Language Toolkit)

To install NLTK, use pip:

```bash
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:

```python
import nltk
nltk.download('words')
```

Then install Streamlit using pip:

```bash
pip install streamlit
```

You can install all the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

After following the installation steps, you can run the Streamlit web app as follows:

```sh
streamlit run app.py
```

This will open a web page in your default browser running on your localhost.

---
<p align="center">👧 Author: <b>Mina Jazini</b></p>