from geopy.geocoders import Nominatim
from dataclasses import dataclass

@dataclass
class PersonalInfo:
    # Standard API header:
    headers = {
        'SuperUniqueUsername92847264859696432': '(myweatherapp.com, tmprevo@gmail.com)'
    }
    address = "Portland, Oregon"
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(f"{address}")
    latitude = location.latitude
    longitude = location.longitude

    # # ALTERNATE: User-defined API header:
    # address = input("Input your street address, city, state: ") # TODO: Error handling unclear, but city/state acceptable as well
    # username = input("Input-a-unique-username8213500-no-spaces-or-special-characters")
    # email = input("youraddress@email.com")
    # headers = {
    #     f'{username}': f'(myweatherapp.com, {email})'
    # }


# print(f"Latitude: {PersonalInfo.latitude}, Longitude: {PersonalInfo.longitude}")