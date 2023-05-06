class RentCarService:
    def __init__(self, numb: int, brand: str, year: int, color: str, power: int, status: bool = False):
        self.__numb = numb
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__power = power
        self.__status = status

    @property
    def numb(self):
        return self.__numb

    @property
    def brand(self):
        return self.__brand

    @property
    def year(self):
        return self.__year
    @property
    def color(self):
        return self.__color
    @property
    def power(self):
        return self.__power


    def str(self):
        return f"ID-номер машины:{self.__numb}, марка: {self.__brand}, год: {self.__year}," \
               f" цвет: {self.__color}, мощность {self.__power}, статус автомобиля:{self.__status}"


class PrintCarService:
    def __init__(self, numb: int, date: str, time: str):
        self.__numb = numb
        self.__date = date
        self.__time = time

    @staticmethod
    def print_car(numb: int, date: str, time: str):
        print(f"Заказ на бронирование:"
              f" Машина по ID-номеру:{numb},взята в аренду {date} на время: {time}")


class CarInfoService:
    @staticmethod
    def info_car(id: int, brand: str, year: int, color: str, power: int):
        print(f"Информация о данном автомобиле:\nID-номер автомобиля:{id}, марка: {brand}, год: {year},"
              f" цвет: {color}, мощность {power} ")


class NotificationService:


    @staticmethod
    def send_sms(telephone):
        print(f"Смс сообщение отправлено на номер абонента {telephone}: ")


class CarService:
    def __init__(self):
        self.__list = []

    def add_car(self, car: RentCarService):
        self.__list.append(car)

    def remove_car(self, car: RentCarService):
        self.__list.remove(car)

    def find_car_by_id(self, numb: int):
        for car in self.__list:
            if car.numb == numb:
                return car
        return None




def execute_application():
    list_car =[]

    car_service = CarService()

    car1 = RentCarService(1001, "Toyota", 2020, "black", 200)
    car2 = RentCarService(1002, "BMW", 2018, "white", 250)
    car3 = RentCarService(1003, "Mercedes", 2019, "silver", 220)
    car_service.add_car(car1)
    car_service.add_car(car2)
    car_service.add_car(car3)


    print(f"Поиск тачки: ")



    # Поиск автомобиля по ID-номеру
    car_id = 1002
    found_car = car_service.find_car_by_id(car_id)
    if found_car:
        print(f"Найден автомобиль с номером {found_car.numb}, марки {found_car.brand}, цвета {found_car.color}, \n"
              f"года {found_car.year}, мощностью {found_car.power} л.с.")
    else:
        print(f"Автомобиль с ID-номером {car_id} не найден")

    # # Бронирование автомобиля
    date = "23.06.2023"
    time = "2 days"
    booked_car = car_service.find_car_by_id(car_id)

    if booked_car:
        #booked_car._RentCarService__status = True
        PrintCarService.print_car(car_id,date,time)
        NotificationService.send_sms("8(927)653-77-25")
    else:
        print(f"Автомобиль с ID-номером {car_id} не найден")


if __name__ == "__main__":
    execute_application()

