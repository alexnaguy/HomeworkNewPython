import pickle
import json

# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.
class Car:

    def __init__(self, name: str, manufacturer: str, engine_volume : str, color: str = None  ):

        self.__name = name
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color

    def __str__(self):
        return f"Название модели: {self.__name} \n" \
               f"Производитель: {self.__manufacturer} \n" \
               f"Обьм двигателя: {self.__engine_volume} \n" \
               f"Цвет: {self.__color}"

#Геттер сеттеры

# Назавание модели
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name: str ):
        self.__name = name

# Производитель
    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

# ббъем двигателя
    @property
    def engine_volume(self):
        return self.__engine_volume
    @engine_volume.setter
    def engine_volume(self, engine_volume: str):
        self.__engine_volume = engine_volume
# Цвет

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color


class PickleCarAdapter:

    @staticmethod
    def save_pickle(car: Car):
        if isinstance(car, Car):
            return pickle.dumps({
                    "Марка автомобиля": car.name,
                    "Производитель": car.manufacturer,
                    "Объем двигателя": car.engine_volume,
                    "Цвет": car.color,
                })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        return obj

class JsonCarAdapter:

    @staticmethod
    def save_json(car: Car):
        if isinstance(car, Car):
            return json.dumps({
                    "Марка автомобиля": car.name,
                    "Производитель": car.manufacturer,
                    "Объем двигателя": car.engine_volume,
                    "Цвет": car.color,
                })

    @staticmethod
    def from_json(data):
        obj = json.loads(data)
        return obj
