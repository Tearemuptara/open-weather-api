import json
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class PlantInfo:
    name: str
    ideal: bool = False
    date: str = ""

@dataclass
class MonthActivities:
    seed_indoor: List[PlantInfo] = field(default_factory=list)
    seed_outdoor: List[PlantInfo] = field(default_factory=list)
    starts: List[PlantInfo] = field(default_factory=list)

@dataclass
class Month:
    name: str
    activities: MonthActivities = field(default_factory=MonthActivities)

def process_plant_data(data: Dict[str, Any]) -> List[Month]:
    months = []
    annual_data = data['annual_data_PDX']['months']

    for month_data in annual_data:
        month = Month(name=month_data['name'])
        activities = month_data.get('activities', {})

        for activity_type in ['seed_indoor', 'seed_outdoor', 'starts']:
            plants = activities.get(activity_type, [])
            if isinstance(plants, dict):  # Handle nested structure (e.g., "late_april")
                plants = [item for sublist in plants.values() for item in sublist]

            for plant in plants:
                if isinstance(plant, dict):
                    plant_info = PlantInfo(
                        name=plant['name'],
                        ideal=plant.get('ideal', False),
                        date=plant.get('date', '')
                    )
                else:
                    plant_info = PlantInfo(name=plant)
                
                getattr(month.activities, activity_type).append(plant_info)

        months.append(month)

    return months

def main():
    with open('plant_data_claude.json', 'r') as file:
        data = json.load(file)

    months = process_plant_data(data)

    # Print the processed data
    for month in months:
        print(f"\n{month.name}:")
        for activity_type in ['seed_indoor', 'seed_outdoor', 'starts']:
            plants = getattr(month.activities, activity_type)
            if plants:
                print(f"  {activity_type.replace('_', ' ').capitalize()}:")
                for plant in plants:
                    info = f"    - {plant.name}"
                    if plant.ideal:
                        info += " (ideal)"
                    if plant.date:
                        info += f" (date: {plant.date})"
                    print(info)

if __name__ == "__main__":
    main()