import pickle
import json
import math

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

# Задача 3
class Fraction:

    def __init__(self,numerator: int, denominator:int):
        self.__nod = math.gcd(numerator,denominator)
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

# +
    def __is_fraction(self, other):
        if not isinstance(other,Fraction):
            raise TypeError(f"Невозможно выполнить сравнение "
                            f"между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __easy_fraction(self, other):
        if self.__denominator == other.__denominator:
            new_denominator = self.__denominator
            new_numerator = self.__numerator + other.__numerator
            return f"{new_numerator} / {new_denominator}"



    def __int_result(self):
        """
        Вернет целое число от деления числителя на знаменатель
        :param other:
        :return:
        """
        if self.__numerator % self.__denominator == 0:
            res = self.__numerator / self.__denominator
            return round(res)

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"

class PickleFraction:

    @staticmethod
    def save_pickle(fraction: Fraction):
        if isinstance(fraction, Fraction):
            return pickle.dumps({
                    "Числитель": fraction.numerator,
                    "Знаменаель": fraction.denominator,

                })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        return obj

class JsonFraction:

    @staticmethod
    def save_json(fraction: Fraction):
        if isinstance(fraction, Fraction):
            return json.dumps({
                    "Числитель": fraction.numerator,
                    "Знаменатель": fraction.denominator,

                })
    @staticmethod
    def from_json(data):
        obj = json.loads(data)
        return obj

class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @classmethod
    def create_time(cls, hour: int, minute: int, second: int):
        # TODO: перевести часы, минуты, секунды -> секунды
        pass

    def __is_time(self, other):
        if not isinstance(other, Time):
            raise TypeError(f"Невозможно выполнить сравнение "
                            f"между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")


class PickleTime:
    @staticmethod
    def save_pickle(time : Time):
        if isinstance(time, Time):
           return pickle.dumps({
               "Часы": {time.hours},
               "Минуты": {time.minutes},
               "Ctreyls": {time.seconds}
           })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        return obj

class JsonTime:

    @staticmethod
    def save_json(time : Time):
        if isinstance(time, Time):
           return json.dumps({
               "Часы": {time.hours},
               "Минуты": {time.minutes},
               "Ctreyls": {time.seconds}
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
    print()
    #Задача 3
    fract1 = Fraction(4, 9)
    res = PickleFraction.save_pickle(fract1)
    print(f"При сериализации объекта Fraction через Pickle получилось {res}")
    obj = PickleFraction.from_pickle(res)
    print(f"После десириализации {obj}")

    res = JsonFraction.save_json(fract1)
    print(f"При сериализации объекта Fraction через Json получилось {res}")
    obj = JsonFraction.from_json(res)
    print(f"После десириализации {obj}")

    #Задача 4
    time = Time(11,45,27)
    res = PickleTime.save_pickle(time)
    print(f"При сериализации объекта Time через Pickle получилось {res}")
    obj = PickleTime.from_pickle(res)
    print(f"После десириализации {obj}")

    res = JsonTime.save_json(time)
    print(f"При сериализации объекта Time через Json получилось {res}")
    obj = JsonTime.from_json(res)
    print(f"После десириализации {obj}")


if __name__ == "__main__":
    execute_appliation()