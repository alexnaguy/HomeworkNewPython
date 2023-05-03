class RentCarService:
    def __init__(self, id: int, brand: str, year: int, color: str, power: int, status: bool = False):
        self.__id = id
        self.brand = brand
        self.year = year
        self.color = color
        self.power = power
        self.status = status

    @property
    def id(self):
        return self.__id

    def str(self):
        return f"ID-номер машины:{self.__id}, марка: {self.brand}, год: {self.year}," \
               f" цвет: {self.color}, мощность {self.power}, статус автомобиля:{self.status}"


class PrintCarService:
    def __init__(self, id: int, date: str, time: str):
        self.id = id
        self.date = date
        self.time = time

    @staticmethod
    def print_car(id: int, date: str, time: str):
        print(f"Заказ на бронирование:"
              f" Машина по ID-номеру:{id},взята в аренду {date} на время: {time}")


class CarInfoService:
    @staticmethod
    def info_car(id: int, brand: str, year: int, color: str, power: int):
        print(f"Информация о данном автомобиле:\nID-номер автомобиля:{id}, марка: {brand}, год: {year},"
              f" цвет: {color}, мощность {power} ")


class NotificationService:
    def __init__(self, telephone: str):
        self.telephone = telephone

    @staticmethod
    def send_sms(telephone, brand, year, color):
        print(f"Смс сообщение отправлено на номер абонента {telephone}: "
              f"Ваш автомобиль {brand}, {year} года, {color} цвета")


class CarService:
    def __init__(self):
        self.__list = []

    def add_car(self, car: RentCarService):
        self.__list.append(car)

    def remove_car(self, car: RentCarService):
        self.__list.remove(car)

    def find_car_by_id(self, number: int):
        for element in self.__list:
            if element.id == number:
                return element
        return None

    # def find_car_by_brand_and_year(self, brand: str, year: int):
    #     for car in self.__list:
    #         if car.brand == brand and car.year == year:
    #             return car
    #     return None


def execute_application():
    car_service = CarService()
    car1 = RentCarService(1001, "Toyota", 2020, "black", 200)
    car2 = RentCarService(1002, "BMW", 2018, "white", 250)
    car3 = RentCarService(1003, "Mercedes", 2019, "silver", 220)
    car_service.add_car(car1)
    car_service.add_car(car2)
    car_service.add_car(car3)

    # Поиск автомобиля по ID-номеру
    car_id = 1003
    found_car = car_service.find_car_by_id(car_id)
    if found_car:
        CarInfoService.info_car(found_car.id, found_car.brand, found_car.year, found_car.color, found_car.power)
    else:
        print(f"Автомобиль с ID-номером {car_id} не найден")

    # Бронирование автомобиля
    car_id = 1001
    date = "23.06.2023"
    time = "2 days"
    booked_car = car_service.find_car_by_id(car_id)

    if booked_car:
        #booked_car._RentCarService__status = True
        PrintCarService.print_car(car_id,date,time)
        NotificationService.send_sms("8(927)653 77 25", booked_car.brand, booked_car.year, booked_car.color)
    else:
        print(f"Автомобиль с ID-номером {car_id} не найден")


if __name__ == "__main__":
    execute_application()

