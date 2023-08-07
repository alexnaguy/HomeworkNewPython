from counry_dict import *
import json
# Создаем словарь данных
data_dict = {'Russia': 'Moscow', 'France': 'Paris'}

# Добавляем данные
add_data(data_dict, 'Germany', 'Berlin')
add_data(data_dict, 'Japan', 'Tokyo')
print(data_dict)

# Редактируем данные
edit_data(data_dict, 'Russia', 'Saint Petersburg')
print(data_dict)
# Сохраняем данные в файл
file_name = "country_new"
with open(file_name, 'w') as write_file:
    json.dump(data_dict, write_file)

# Загружаем данные из файла
loaded_data = load_data(file_name)

#Выводим загруженные данные
print(f"Загруженные данные:")
for country, capital in loaded_data.items():
    print(f"Country: {country}, Capital: {capital}")