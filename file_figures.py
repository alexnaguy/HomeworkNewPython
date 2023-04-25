from figures import *

class ManagerFigures:

    def write_file(self, path: str):
        """
        Запись в файл информации о данной фигуре

        :param path: Путь к файлу с наванием
        :param text: Информация о фигуре (классе)
        :return:
        """
        with open(path, "w", encoding="utf-8") as file:
            for value in self.__dict__.values():
                file.write(str(value) + "\n")


    def read_square_from_file(self,path):
        with open(path, "r", encoding="utf-8") as file:
            x = file.readline().rstrip("\n")
            y = file.readline().rstrip("\n")
            side = file.readline().rstrip("\n")
            return x , y, side

    def read_rectangle_from_file(self,path):
        with open(path, "r", encoding="utf-8") as file:
            x = file.readline().rstrip("\n")
            y = file.readline().rstrip("\n")
            width = file.readline().rstrip("\n")
            height = file.readline().rstrip("\n")
            return x , y, width, height


    def read_circle_from_file(self,path):
        with open(path, "r", encoding="utf-8") as file:
            x = file.readline().rstrip("\n")
            y = file.readline().rstrip("\n")
            radius = file.readline().rstrip("\n")
            return x , y, radius

    def read_ellipse_from_file(self, path):
        with open(path, "r", encoding="utf-8") as file:
            x = file.readline().rstrip("\n")
            y = file.readline().rstrip("\n")
            width = file.readline().rstrip("\n")
            height = file.readline().rstrip("\n")
            return x, y, width, height
