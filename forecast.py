import requests
#import json
from dataclasses import dataclass

#Define a data class
@dataclass
class Forecast:
    day: str
    temperature: int
    chance_rain: int


headers = {
    'Happy-Agent50371376785416137261': '(myweatherapp.com, tmprevo@gmail.com)'
}

#Zone-county correlation file: https://www.weather.gov/gis/ZoneCounty
latitude = 39.7456
longitude = -97.0892

#url = f'https://api.weather.gov/points/{latitude},{longitude}'
url = 'https://api.weather.gov/gridpoints/TOP/31,80/forecast'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    forecast = [
        Forecast(
            day = period['name'],
            temperature = period['temperature'],
            chance_rain = period['probabilityOfPrecipitation']['value'],
        )
        for period in data['properties']['periods']
    ]

    for f in forecast:
        print(f.day)
        print(f.temperature)
        print(f.chance_rain)

    #stuff = json.dumps(data, indent=4)
    #print(stuff)
else: print("Error.")