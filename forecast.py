import requests
import json
from dataclasses import dataclass
from geolocation import PersonalInfo
from forecast_metadata import get_forecast_metadata

#Define the forecast data class
@dataclass
class Forecast:
    day: str
    temperature: int
    chance_rain: int

def get_forecast():
    headers = PersonalInfo.headers
    url = get_forecast_metadata()
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
            print(f'{f.day}: {f.temperature} degrees)')
            if f.chance_rain != None: print(f'{f.chance_rain}% chance of rain') 
            else: print("No rain!")

        # stuff = json.dumps(data, indent=4)
        # print(stuff)
    else: print("Error.")


get_forecast()