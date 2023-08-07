from music_dict import *

 #Создаем список данных

def execute_aplication():

    music_list = []

    # Добавляем данные
    add_data(music_list,"КИШ","Камнем по голове")
    add_data(music_list,"КИШ","Старый дом")
    add_data(music_list,"КИШ","Лесник")
    #print(music_list)


    # Удаляем данные
    remove_data(music_list,"Лесник")
    #print(music_list)

    # Сохраняем данные в файл
    name_file = 'music_collection.json'
    save_data(music_list, name_file)

    # Загружаем данные из файла
    print(f"Загруженные данные из файла {name_file}: ")
    loaded_data = load_data(name_file)

    # Выводим на экран
    print(f"Список исполнителей и песен:")
    for item in loaded_data:
        print(f"Исполнитель: {item['Исполнитель']}, Песня: {item['Песня']}")


if __name__ == '__main__':
    execute_aplication()