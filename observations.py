import requests
import json

# headers = {
#     'Happy-Agent50371376785416137261': '(myweatherapp.com, tmprevo@gmail.com)'
# }

#Zone-county correlation file: https://www.weather.gov/gis/ZoneCounty
latitude = 45.4718
longitude = -122.9062
zoneId = "PQR"

points_url = "https://api.weather.gov/zones/forecast/{zoneId}/observations"
response = requests.get(points_url)

if response.status_code == 200:
    data = response.json()
    #Pretty print the full response from the endpoint:
    print("Full /points response:")
    print(json.dumps(data, indent=4))
