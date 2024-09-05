import json

def load_stations(file_path):
    with open(file_path) as f:
        data = json.load(f)
        if isinstance(data, dict):
            stations = data.get('payload', [])
        elif isinstance(data, list):
            stations = data
        else:
            stations = []
    return stations

def print_station_info(stations):
    print('Dit zijn de namen, codes en types van elk station:')
    for station in stations:
        print(f"{station['namen']['lang']} - {station['code']} : {station['stationType']}")

def find_most_easterly_station(stations):
    most_easterly_station = max(stations, key=lambda x: x['lng'])
    return most_easterly_station

stations = load_stations('stations.json')
print_station_info(stations)

most_easterly_station = find_most_easterly_station(stations)
print(f"\nHet meest oostelijk gelegen station is: {most_easterly_station['namen']['lang']}")