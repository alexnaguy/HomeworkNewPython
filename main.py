
class RentCarService:
    pass

class PrintCarService:
    pass

class CarInfoService:
    pass
class NotificationService:
    pass

class CarService:
    pass

class Car():
    def __init__(self,id:int, brand: str, year: int, color: str, power: int):
        self.__id = id
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__power = power


    def __str__(self):
        return f" ID-номер машины:{self.__id}  марка: {self.__brand} год: {self.__year} цвет: {self.__color}"


def execute_application():
    pass

if __name__ == "__main__":
    execute_application()