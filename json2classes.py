# import json
# from dataclasses import dataclass, field, is_dataclass
# from typing import List, Optional, Dict, Any

# # Define data classes corresponding to the JSON structure
# @dataclass
# class ProbabilityOfPrecipitation:
#     unitCode: str
#     value: Optional[float]

# @dataclass
# class Elevation:
#     unitCode: str
#     value: float

# @dataclass
# class Period:
#     number: int
#     name: str
#     startTime: str
#     endTime: str
#     isDaytime: bool
#     temperature: int
#     temperatureUnit: str
#     temperatureTrend: Optional[str]
#     probabilityOfPrecipitation: Optional[ProbabilityOfPrecipitation]
#     windSpeed: str
#     windDirection: str
#     icon: str
#     shortForecast: str
#     detailedForecast: str

# @dataclass
# class Properties:
#     units: str
#     forecastGenerator: str
#     generatedAt: str
#     updateTime: str
#     validTimes: str
#     elevation: Elevation
#     periods: List[Period]

# @dataclass
# class Geometry:
#     type: str
#     coordinates: List

# @dataclass
# class Feature:
#     context: List
#     type: str
#     geometry: Geometry
#     properties: Properties

# def from_dict(cls, data):
#     """Recursively instantiate data classes from a dictionary."""
#     if not is_dataclass(cls):
#         return data
#     fieldtypes = {f.name: f.type for f in cls.__dataclass_fields__.values()}
#     kwargs = {}
#     for field, fieldtype in fieldtypes.items():
#         if field in data:
#             value = data[field]
#             if hasattr(fieldtype, '__origin__'):
#                 # Handle typing.Optional, typing.List, etc.
#                 if fieldtype.__origin__ in (list, List):
#                     item_type = fieldtype.__args__[0]
#                     value = [from_dict(item_type, item) if isinstance(item, dict) else item for item in value]
#                 elif fieldtype.__origin__ in (dict, Dict):
#                     pass  # Keep as is
#                 elif fieldtype.__origin__ is Union and type(None) in fieldtype.__args__:
#                     inner_type = fieldtype.__args__[0]
#                     if isinstance(value, dict):
#                         value = from_dict(inner_type, value)
#             elif is_dataclass(fieldtype):
#                 value = from_dict(fieldtype, value)
#             kwargs[field] = value
#     return cls(**kwargs)

# def rename_keys(obj, key_mapping):
#     """Recursively rename keys in dictionaries according to a mapping."""
#     if isinstance(obj, list):
#         return [rename_keys(item, key_mapping) for item in obj]
#     elif isinstance(obj, dict):
#         new_obj = {}
#         for k, v in obj.items():
#             new_key = key_mapping.get(k, k)
#             new_obj[new_key] = rename_keys(v, key_mapping)
#         return new_obj
#     else:
#         return obj

# # Replace 'your_json_string' with your actual JSON data as a string
# your_json_string = '''
# {
#     "@context": [
#         "https://geojson.org/geojson-ld/geojson-context.jsonld",
#         {
#             "@version": "1.1",
#             "wx": "https://api.weather.gov/ontology#",
#             "geo": "http://www.opengis.net/ont/geosparql#",
#             "unit": "http://codes.wmo.int/common/unit/",
#             "@vocab": "https://api.weather.gov/ontology#"
#         }
#     ],
#     "type": "Feature",
#     "geometry": {
#         "type": "Polygon",
#         "coordinates": [
#             [
#                 [
#                     -122.6880785,
#                     45.5346378
#                 ],
#                 [
#                     -122.6819138,
#                     45.513782299999995
#                 ],
#                 [
#                     -122.6521851,
#                     45.51809349999999
#                 ],
#                 [
#                     -122.6583436,
#                     45.53894919999999
#                 ],
#                 [
#                     -122.6880785,
#                     45.5346378
#                 ]
#             ]
#         ]
#     },
#     "properties": {
#         "units": "us",
#         "forecastGenerator": "BaselineForecastGenerator",
#         "generatedAt": "2024-10-19T03:16:24+00:00",
#         "updateTime": "2024-10-19T02:41:50+00:00",
#         "validTimes": "2024-10-18T20:00:00+00:00/P7DT8H",
#         "elevation": {
#             "unitCode": "wmoUnit:m",
#             "value": 60.96
#         },
#         "periods": [
#             {
#                 "number": 1,
#                 "name": "Tonight",
#                 "startTime": "2024-10-18T20:00:00-07:00",
#                 "endTime": "2024-10-19T06:00:00-07:00",
#                 "isDaytime": false,
#                 "temperature": 54,
#                 "temperatureUnit": "F",
#                 "temperatureTrend": "",
#                 "probabilityOfPrecipitation": {
#                     "unitCode": "wmoUnit:percent",
#                     "value": 70
#                 },
#                 "windSpeed": "6 mph",
#                 "windDirection": "SSE",
#                 "icon": "https://api.weather.gov/icons/land/night/rain,70/rain,40?size=medium",
#                 "shortForecast": "Light Rain Likely",
#                 "detailedForecast": "Rain likely. Cloudy, with a low around 54. South southeast wind around 6 mph. Chance of precipitation is 70%."
#             },
#             // ... include the rest of your periods here ...
#         ]
#     }
# }
# '''

# # Load the JSON data
# data = json.loads(your_json_string)

# # Map JSON keys to valid Python identifiers
# key_mapping = {
#     "@context": "context",
#     "@version": "version",
#     "@vocab": "vocab"
# }

# # Rename keys in the data according to the mapping
# data = rename_keys(data, key_mapping)

# # Convert the dictionary to data class instances
# feature = from_dict(Feature, data)

# # Now you can access the data using object properties
# # For example, print the detailed forecast of the first period
# print(feature.properties.periods[0].detailedForecast)
