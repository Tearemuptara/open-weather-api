from enum import Enum
import pandas as pd
from dataclasses import dataclass

file_path = 'C:\\Users\\TearE\\code\\open-weather-api\\pdxnursery_data.xlsx'

xls = pd.ExcelFile(file_path)

sheet_names = xls.sheet_names

plants_by_period = pd.read_excel(xls, sheet_name='plants by period')
columns = plants_by_period.columns
print(columns)
overwintering = pd.read_excel(xls, sheet_name='overwintering')
ideal_planting = pd.read_excel(xls, sheet_name='ideal planting')

print(plants_by_period)

@dataclass
class Plant:
    name: str
    overwinter: bool
    mulch: bool
    cover: bool

# # TODO: Extend plants to specifically MyPlants
# class MyPlant(Plant):
#     def __init__(self, name, overwinter, mulch, cover, location, date_planted, nickname=None):
#         # Use the superclass initializer for common properties
#         super().__init__(name, overwinter, mulch, cover)
#         # Add specific data for your plant
#         self.location = location
#         self.date_planted = date_planted
#         self.nickname = nickname


@dataclass
class SeasonalPeriod:
    period_name: str
    seed_indoor: list[Plant]
    seed_outdoor: list[Plant]
    plant_starts: list[Plant]

