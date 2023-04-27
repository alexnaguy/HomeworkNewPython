
class RentCarService:
    def __init__(self, id: int, brand: str, year: int, color: str, power: int):

        self.__id = id
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__power = power


    def __str__(self):
        return f" ID-номер машины:{self.__id}, марка: {self.__brand}, год: {self.__year}," \
               f" цвет: {self.__color}, мощность {self.__power}"


class PrintCarService:
    def __init__(self, id: int,date: str, time: str):
        self.__id = id
        self.__date = date
        self.__time = time

    @staticmethod
    def print_car( id: int, date : str, time: str):
        print( f"Заказ на броинрвоание:" \
               f" Машина по ID-номеру:{id},взята в аренду {date} на время: {time}")


class CarInfoService:
    def __init__(self, id: int, brand: str, year: int, color: str, power: int):
        self.__id = id
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__power = power
    @property
    def id(self,):
        return self.__id
    #def info_car(self, id: int, brand: str, year: int, color: str, power: int):


class NotificationService:
    def __int__(self, id: int, brand: str, year: int, color: str, telephone: str):
        self.__id = id
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__telephone = telephone

    def send_sms(self,telephone, brand, year, color):
        print(f"Смс сообщение отпрвлено на номер абонента {self.__telephone} : "
              f"Ваш автомобиль {self.__brand}, {self.__year} года, {self.__color} цвета")

class CarService:
    def __init__(self, id: int, brand: str):
        self.__id = id
        self.__brand = brand
    @property
    def id(self,):
        return self.__id

    #def info_number_car(self, id: int, brand: str ):








def execute_application():
    list_car = []
    car1 = RentCarService(10001,"BMW",2018, "red", 220)
    car2 = RentCarService(10002, "Renault", 2021, "blue", 98)
    car3 = RentCarService(10003," Skoda", 2015, "black", 150)
    car4 = RentCarService(10004, "Mersedea", 2023, "red", 170)
    list_car.append(car1)
    list_car.append(car2)
    list_car.append(car3)
    list_car.append(car4)
    for car in list_car:
        print(car)

    PrintCarService.print_car(10001,"22.03.2023", "4 дня")
    NotificationService.send_sms()









if __name__ == "__main__":
    execute_application()