import requests


def county_info(country_name : str)->str:
    
    url=f"https://restcountries.com/v3.1/name/{country_name}"
    response=requests.get(url)
    
    if response.status_code != 200:
        return None
    
    data=response.json()[0]
    capital = data['capital'][0]
    region = data['region']
    flag =data['flags']['png']
    languages = ",".join(data.get('languages', {}).values())
    population = data['population']
    currencies_data=data['currencies']
    currencies=','.join([f'{cur} , Symbol of Currency : {info['symbol']}, Name of Currency : {info['name']}' for cur,info in currencies_data.items()])
   
    return {"Capital": capital,
        "Region": region,
        "Flag": flag,
        "Languages": languages,
        "Population": population,
        "Currencies": currencies}


if __name__=='__main__':
    your_country=input('Please write Your Country:')
    print(county_info(your_country))