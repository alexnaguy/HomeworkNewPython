import json

def add_data(data_list, artist, song):
    data_list.append({'Исполнитель': artist, 'Песня': song})

def remove_data(data_list, song, artist = None ):
    for item in data_list:
        if item['Исполнитель'] == artist or item['Песня'] == song:
            data_list.remove(item)
        else:
            "Не нашли"

def save_data(data_list, filename):
    with open(filename, 'w') as file:
        json.dump(data_list, file)

def load_data(filename):
    with open(filename, 'r') as file:
        data_list = json.load(file)
    return data_list