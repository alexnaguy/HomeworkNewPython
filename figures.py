from abc import ABC, abstractmethod
from file_figures import *
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

class Square(Shape, ManagerFigures):
    __NAME = "Квадрат"

    def __init__(self, x: int, y: int, side: float):
        super().__init__(x, y)
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side

    def info(self):
        super().info()
        print(f"Данная фигура: {self.__NAME}"
              f" cо стороной: {self.__side}\n")

class Rectangle(Shape,ManagerFigures):
    __NAME = "Прямоугольник"

    def __init__(self, x: int, y: int, width: float, height: float):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.__height = height

    def info(self):
        super().info()
        print(f"Данная фигура: {self.__NAME}"
              f" c шириной: {self.__width} и высоой: {self.__height}\n")

class Circle(Shape, ManagerFigures):
    __NAME = "Круг"

    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    radius.setter
    def radius(self, radius):
        self.__radius = radius

    def show(self):
        return self.__dict__

    def info(self):
        super().info()
        print(f"Данная фигура: {self.__NAME}"
              f" c радиусом: {self.__radius} \n")


class Ellipse(Shape,ManagerFigures):
    __NAME = "Эллипс"

    def __init__(self, x: int, y: int, width: float, height: float):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.__height = height

    def info(self):
        super().info()
        print(f"Данная фигура: {self.__NAME}"
              f" c размерами : {self.__width} и {self.__height} \n")

