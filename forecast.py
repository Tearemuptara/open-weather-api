import requests
import json
from dataclasses import dataclass
from business_logic import API_HEADER
from typing import List, Optional

#Define the forecast data class
@dataclass
class Forecast:
    number: int
    name: str
    start_time: str
    end_time: str
    is_daytime: bool
    temperature: Optional[int]
    temperature_unit: str
    temperature_trend: Optional[str]
    probability_of_precipitation: Optional[float]
    wind_speed: str
    wind_direction: str
    icon: str
    short_forecast: str
    detailed_forecast: str

def get_forecast(forecast_url: str) -> List[Forecast]:
    print(f"Fetching forecast data from: {forecast_url}")
    response = requests.get(forecast_url)
    
    if response.status_code == 200:
        data = response.json()
        forecasts = []
        for period in data['properties']['periods']:
            forecast = Forecast(
                number=period.get('number'),
                name=period.get('name'),
                start_time=period.get('startTime'),
                end_time=period.get('endTime'),
                is_daytime=period.get('isDaytime'),
                temperature=period.get('temperature'),
                temperature_unit=period.get('temperatureUnit'),
                temperature_trend=period.get('temperatureTrend') or None,
                probability_of_precipitation=(
                    period.get('probabilityOfPrecipitation', {}).get('value')
                    if period.get('probabilityOfPrecipitation') else None
                ),
                wind_speed=period.get('windSpeed'),
                wind_direction=period.get('windDirection'),
                icon=period.get('icon'),
                short_forecast=period.get('shortForecast'),
                detailed_forecast=period.get('detailedForecast'),
            )
            forecasts.append(forecast)
        
        # Optionally, print out detailed forecasts
        for f in forecasts:
            print(f"{f.name}: {f.detailed_forecast}\n")
        
        return forecasts
    else:
        print(f"Error fetching data: HTTP {response.status_code}")
        return []