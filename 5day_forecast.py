import requests
import json
#Define User Agent with a unique string.
#Add contact info to be notified by weather.gov of security events.
headers = {
    'Happy-Agent50371376785416137261': '(myweatherapp.com, tmprevo@gmail.com)'
}

latitude = 39.7456
longitude = -97.0892

#Make a request to the endpoint
points_url = f'https://api.weather.gov/points/{latitude},{longitude}'
response = requests.get(points_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # #Pretty print the full response from the /points endpoint:
    print("Full /points response:")
    print(json.dumps(data, indent=4))

    # #Extract the forecast URL from the JSON response
    # forecast_url = data['properties']['forecast']
    # #Fetch the forecast data
    # forecast_response = requests.get(forecast_url, headers=headers)

    # if forecast_response.status_code == 200:
    #     forecast_data = forecast_response.json()
    #     #Print forecast data
    #     for period in forecast_data['properties']['periods']:
    #         print(f"{period['name']}: {period['detailedForecast']}")
    # else:
    #     print(f"Error fetching forecast: {forecast_response.status_code}")

