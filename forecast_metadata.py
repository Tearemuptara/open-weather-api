import requests
import json
from dataclasses import dataclass
from geolocation import PersonalInfo

#Define the forecast data class
@dataclass
class ForecastMetadata:
    forecast_url: str


def get_forecast_metadata():
    url = f'https://api.weather.gov/points/{PersonalInfo.latitude},{PersonalInfo.longitude}'
    response = requests.get(url, headers=PersonalInfo.headers)
    if response.status_code == 200:
        ## Store the response as a .json, optional print
        data = response.json()
        forecast_metadata = json.dumps(data, indent=4)
        # print(forecast_metadata)

        # Extract required variables:
        forecast_url = data['properties']['forecast']
        print(forecast_url)
        return forecast_url
    else: print("Error.")