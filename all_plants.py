import json
from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class PlantInfo:
    name: str
    seed_indoor: List[str] = field(default_factory=list)
    seed_outdoor: List[str] = field(default_factory=list)
    plant_starts: List[str] = field(default_factory=list)
    ideal: List[Tuple[str, str]] = field(default_factory=list)

def extract_plant_info(data):
    plants = {}
    annual_data = data['annual_data_PDX']['months']

    for month_data in annual_data:
        month = month_data['name']
        activities = month_data.get('activities', {})

        for activity_type, plants_list in activities.items():
            if isinstance(plants_list, list):
                process_plants(plants_list, month, activity_type, plants)
            elif isinstance(plants_list, dict):
                for sub_activity, sub_plants in plants_list.items():
                    full_activity = f"{activity_type}_{sub_activity}"
                    process_plants(sub_plants, month, full_activity, plants)

    return plants

def process_plants(plants_list, month, activity, plants_dict):
    for plant in plants_list:
        if isinstance(plant, dict):
            plant_name = plant['name']
            is_ideal = plant.get('ideal', False)
        else:
            plant_name = plant
            is_ideal = False

        if plant_name not in plants_dict:
            plants_dict[plant_name] = PlantInfo(name=plant_name)

        plant_info = plants_dict[plant_name]

        if activity.startswith('seed_indoor'):
            plant_info.seed_indoor.append(month)
            if is_ideal:
                plant_info.ideal.append(('seed_indoor', month))
        elif activity.startswith('seed_outdoor'):
            plant_info.seed_outdoor.append(month)
            if is_ideal:
                plant_info.ideal.append(('seed_outdoor', month))
        elif activity.startswith('starts'):
            plant_info.plant_starts.append(month)
            if is_ideal:
                plant_info.ideal.append(('plant_starts', month))

def main():
    with open('plant_data_claude.json', 'r') as file:
        data = json.load(file)

    plants = extract_plant_info(data)

    print("Plant Information:")
    for plant_name, plant_info in sorted(plants.items()):
        print(f"\n{plant_name}:")
        if plant_info.seed_indoor:
            print(f"  Seed Indoor: {', '.join(sorted(set(plant_info.seed_indoor)))}")
        if plant_info.seed_outdoor:
            print(f"  Seed Outdoor: {', '.join(sorted(set(plant_info.seed_outdoor)))}")
        if plant_info.plant_starts:
            print(f"  Plant Starts: {', '.join(sorted(set(plant_info.plant_starts)))}")
        if plant_info.ideal:
            print("  Ideal:")
            for method, month in sorted(set(plant_info.ideal)):
                print(f"    - {method} in {month}")

if __name__ == "__main__":
    main()