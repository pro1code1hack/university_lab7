import json


def write_to_file(data):
    with open('config.json', 'w') as file:
        json.dump(data, file)
