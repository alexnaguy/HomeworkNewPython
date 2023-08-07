import json

def add_data(data_dict, country, capital):
    data_dict = {}
    data_dict[country] = capital

def edit_data(data_dict, country, new_capital):
    if country in data_dict:
        data_dict[country] = new_capital

def save_data(data_dict, filename):
    with open(filename, 'w') as file:
        json.dump(data_dict, file)

def load_data(filename):
    with open(filename, 'r') as file:
        data_dict = json.load(file)
    return data_dict