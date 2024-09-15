import json

def loadJson(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)



def load_stations(file_path):
    last = {"lng": 0}
    data = loadJson(file_path)
    stations = data["payload"]
    print("Dit zijn de namen, codes en types van elk station:")

    for station in stations:
        print(f"{station["namen"]["lang"]} - {station["code"]} : {station["stationType"]}")
        if float(station["lng"]) > float(last["lng"]):
            last = station
            
        
    print(f"Het meest oostelijk gelegen station is: {last["namen"]["lang"]}")


load_stations("stations.json")