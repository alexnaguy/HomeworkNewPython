import math


# Задание 1.
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд
# перегруженных операторов:
# Проверка на равенство радиусов двух окружностей (операция ==, !=);
# Проверка сравнения длин двух окружностей (операции >, <, <=,>=);

class Circle:
    def __init__(self, radius: float):
        self.__radius = radius
        self.__length = 2 * math.pi * self.__radius

    def check_radius(self,radius: float):
        if radius <= 0:
            raise InitializationValueError("Значение радиуса должно быть больше 0")
        return radius



def execute_application:
    pass

if __name__ == "__main__":
    execute_application()