from figures import *
from file_figures import *



def execute_application():
    square = Square(1, 2, 5)
    text = str(square.info())
    path1 = "square"
    square.write_file(path1)

    rectangle = Rectangle(2, 3, 4, 6)
    rectangle.info()
    path2 = "rectangle"
    rectangle.write_file(path2)

    circle = Circle(2, 3, 7)
    circle.info()
    path3 = "Circle"
    circle.write_file(path3)

    ellipse = Ellipse(4, 2, 4, 8)
    ellipse.info()
    path4 = "Ellipse"
    ellipse.write_file(path4)


if __name__ == "__main__":
    execute_application()