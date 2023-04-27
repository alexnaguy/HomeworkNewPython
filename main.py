
class RentCarService:
    def __init__(self, id: int, brand: str, year: int, color: str, power: int):

        self.__id = id
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__power = power


    def __str__(self):
        return f" ID-номер машины:{self.__id}, марка: {self.__brand}, год: {self.__year}, цвет: {self.__color}"


class PrintCarService:
    def __init__(self, id: int,date: str, time: str):
        self.__id = id
        self.__date = date
        self.__time = time
    def __str__(self):
        return f"Заказ на броинрвоание:" \
               f" Машина по ID-номеру:{self.__id},взята в аренду {self.__date} на время: {self.__time}"



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
    def info_car(self, id: int, brand: str, year: int, color: str, power: int):












class NotificationService:
    def __int__(self, id: int, brand: str, year: int, color: str, telephone: str):
        self.__id = id
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__telephone = telephone

    def send_sms(self,id: int, brand: str, year: int, color: str, power: int, telephone: str):
        print(f"Смс сообщение отпрвлено на номер абонента {self.__telephone} : "
              f"Ваш автомобиль {self.__brand}, {self.__year} года, {self.__color} цвета")

class CarService:
    pass




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






if __name__ == "__main__":
    execute_application()