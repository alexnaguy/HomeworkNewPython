# Плоские фгуры
class Shape:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    # Гетеры Сетеры
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def info(self):
        print(f"Координаты точки начала: x:{self.__x}, y:{self.__y}")