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
