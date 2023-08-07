import json

def add_data(data_dict, country, capital):

    data_dict[country] = capital

def update_data(data_dict, country, new_capital):
    if country in data_dict.keys():
        data_dict[country] = new_capital

def save_data(data_dict, filename):
    with open(filename, 'w') as write_file:
        json.dump(data_dict,write_file)

def load_data(filename):
    with open(filename, 'r') as file:
        data_dict = json.load(file)
    return data_dict