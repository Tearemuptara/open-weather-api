import requests
import json
from dataclasses import dataclass
from business_logic import API_HEADER
from typing import List, Optional

#Define the forecast data class
@dataclass
class Forecast_Metadata:
    forecast_url: str
    grid_id: str
    grid_x: int
    grid_y: int
    forecast_hourly_url: str
    forecast_grid_data: str
    observation_stations: str
    relative_location_city: str
    relative_location_state: str
    relative_location_distance: float
    relative_location_bearing: float
    time_zone: str
    radar_station: str

def get_forecast_metadata(latitude: str, longitude: str) -> Optional[Forecast_Metadata]:
    url = f'https://api.weather.gov/points/{latitude},{longitude}'
    response = requests.get(url, headers=API_HEADER)
    if response.status_code == 200:
        data = response.json()
        
        # Uncomment to see full JSON in output
        # print(json.dumps(data, indent=4))
        
        properties = data.get('properties', {})
        
        # Extracting relative location information
        relative_location = properties.get('relativeLocation', {})
        relative_location_properties = relative_location.get('properties', {})
        city = relative_location_properties.get('city')
        state = relative_location_properties.get('state')
        distance = relative_location_properties.get('distance', {}).get('value')
        bearing = relative_location_properties.get('bearing', {}).get('value')
        
        # Create the ForecastMetadata instance
        forecast_metadata = Forecast_Metadata(
            forecast_url=properties.get('forecast'),
            grid_id=properties.get('gridId'),
            grid_x=properties.get('gridX'),
            grid_y=properties.get('gridY'),
            forecast_hourly_url=properties.get('forecastHourly'),
            forecast_grid_data=properties.get('forecastGridData'),
            observation_stations=properties.get('observationStations'),
            relative_location_city=city,
            relative_location_state=state,
            relative_location_distance=distance,
            relative_location_bearing=bearing,
            time_zone=properties.get('timeZone'),
            radar_station=properties.get('radarStation')
        )
        
        # Print the forecast URL (as in your original code)
        print(f"Forecast URL: {forecast_metadata.forecast_url}")
        print(f"Grid ID: {forecast_metadata.grid_id}")
        print(f"Grid X: {forecast_metadata.grid_x}")
        print(f"Grid Y: {forecast_metadata.grid_y}")
        print(f"City: {forecast_metadata.relative_location_city}")
        print(f"State: {forecast_metadata.relative_location_state}")
        print(f"Time Zone: {forecast_metadata.time_zone}")
        print(f"Forecast Hourly url: {forecast_metadata.forecast_hourly_url}")
        
        return forecast_metadata
    else:
        print(f"Error: Status code {response.status_code} (not 200) from api.weather.gov.")
        return None