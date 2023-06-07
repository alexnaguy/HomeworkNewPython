import pickle
import json

class Plane:
    def __init__(self, model:str, length: float, weight: int, passengers: int):
        self.__model = model
        self.__length = length
        self.__weight = weight
        self.__passengers = passengers

    @property
    def model(self):
        return self.__model

    @property
    def length(self):
        return self.__length

    @property
    def weight(self):
        return self.__weight

    @property
    def passengers(self):
        return self.__passengers

    def __str__(self):
        return f"Модель: {self.__model}\""\
               f"Длина: {self.__length}\"" \
               f"Вес: {self.__weight} \"" \
               f"Пассажиры: {self.__passengers}"

    def to_dict(self):
        return {"Модель самолета": {self.__model}, "Длина": {self.__length},
                "Вес": {self.__weight}, "Пассажиры": {self.__passengers} }


class PicklePlane:
    @staticmethod
    def save_pickle(plane: Plane):
        if isinstance(plane, Plane):
            return pickle.dumps({
                    "Модель": plane.model,
                    "Длина": plane.length,
                    "Вес": plane.weight,
                    "Пассажиры": plane.passengers,
                })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        return obj


class JsonPlane:

    @staticmethod
    def save_json(plane: Plane):
        if isinstance(plane, Plane):
            return json.dumps({
                    "Модель": plane.model,
                    "Длина": plane.length,
                    "Вес": plane.weight,
                    "Пассажиры": plane.passengers,
                })

    @staticmethod
    def from_json(data):
        obj = json.loads(data)
        return obj

def execute_appliation():

    # Задача 1
    plane1 = Plane("Boeing 747",70, 170, 430)
    res = PicklePlane.save_pickle(plane1)
    print(f"При сериализации объекта Plane через Pickle получилось {res}")
    obj = PicklePlane.from_pickle(res)
    print(f"После десериализации объекта получилось {obj}")
    # Задача 2
    res = JsonPlane.save_json(plane1)
    print(f"При сериализации объекта получилось {res}")
    obj = JsonPlane.from_json(res)
    print(f"После десериализации объекта через Json получилось {obj}")


if __name__ == "__main__":
    execute_appliation()