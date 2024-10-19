import requests
import json

headers = {
    'Happy-Agent50371376785416137261': '(myweatherapp.com, tmprevo@gmail.com)'
}

#Zone-county correlation file: https://www.weather.gov/gis/ZoneCounty
latitude = 45.4718
longitude = -122.9062
zoneId = 111

points_url = "https://api.weather.gov/zones/forecast/{zoneId}/observations"
response = requests.get(points_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    #Pretty print the full response from the endpoint:
    print("Full /points response:")
    print(json.dumps(data, indent=4))

    #Extract the forecast URL from the JSON response
    forecast_url = data['properties']['forecast']
    #Fetch the forecast data
    forecast_response = requests.get(forecast_url, headers=headers)

    if forecast_response.status_code == 200:
        forecast_data = forecast_response.json()
        #Print forecast data
        for period in forecast_data['properties']['periods']:
            print(f"{period['name']}: {period['detailedForecast']}")
    else:
        print(f"Error fetching forecast: {forecast_response.status_code}")
