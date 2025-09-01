import streamlit as st
import requests
from country_info import county_info 
import pandas as pd

st.title('🗺️ Country Info')
st.write('View essential information about any country, including its capital, region, flag, languages, population, and currencies. Quickly search and explore countries in one simple app.')



url = "https://restcountries.com/v3.1/all?fields=name"
response = requests.get(url)
data = response.json()
countries = sorted([country['name']['common'] for country in data])

country_name=st.selectbox('Choose Country',countries)
st.write(f'👉 Your choice is',f'"{country_name}".')
info = county_info(country_name)

df = pd.DataFrame({
        "informations": ["Capital", "Region", "Languages", "Population", "Currencies", "Flag"],
        "Value": [
            info["Capital"],
            info["Region"],
            info["Languages"],
            info["Population"],
            info["Currencies"],
            f'<img src="{info["Flag"]}" width="125">'
        ]
    })
st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)