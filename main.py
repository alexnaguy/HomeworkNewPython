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

#Равенство
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.__radius == other.__radius
        raise TypeError(f"Невозможно выполнить сравнение между {self.__class__.__name__} и {other.__class__.__name__}")

# Неравенство
    def __ne__(self, other):
        if isinstance(other, Circle):
            return self.__radius != other.__radius
        raise TypeError(f"Невозможно выполнить сравнение между {self.__class__.__name__} и {other.__class__.__name__}")

# <
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.__length < other.__length
        raise TypeError(f"Невозможно выполнить сравнение между {self.__class__.__name__} и {other.__class__.__name__}")

# <=
    def __le__(self, other):
        if isinstance(other, Circle):
            return self.__length <= other.__length
        raise TypeError(f"Невозможно выполнить сравнение между {self.__class__.__name__} и {other.__class__.__name__}")

# >
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.__length > other.__length
        raise TypeError(f"Невозможно выполнить сравнение между {self.__class__.__name__} и {other.__class__.__name__}")

# <=
    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.__length >= other.__length
        raise TypeError(f"Невозможно выполнить сравнение между {self.__class__.__name__} и {other.__class__.__name__}")

    def __hash__(self):
        return hash((self.__radius, self.__length))

def execute_application:
    # Circle
    print(f"Circle:")
    circle1 = Circle(4)
    circle2 = Circle(6)
    circle1.check_radius(4)
    try:
        print("Проверка на равенство:", circle1 == circle2)
        print("Проверка на не равенство:", circle1 != circle2)
        print("Проверка на меньше", circle1 < circle2)
        print("Проверка на больше:", circle1 > circle2)
        print("Проверка на меньше или равно:", circle1 <= circle2)
        print("Проверка на больше или равно:", circle1 >= circle2)
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    execute_application()