# open-weather-api
Make calls to Weather.gov API to retrieve required data (.json format) for Gardenbook app backend.

Documentation: https://www.weather.gov/documentation/services-web-api

test.json is an example of the API response recieved from this endpoint (and the forecast data available)

1. Fill out the API Header in business_logic.py with contact info for weather.gov to contact you in the event of a security issue with their API service.
2. Main will output a list of 'detailed_forecast' strings.
3. To configure what forecast data is output, see forecast.py. Line 7 of main defaults the location to "Hood River, Oregon" which can be changed to any address or city/state for relevant station lookup.
4. See a full copy of the response json in testoutput.json to see what data is available.