from abc import ABC, abstractmethod
from copy import copy
# Рассмотрим принцип разделения интерфейсов.
# Допустим у нас имеется абстрактный класс Payments и в нем есть три метода:
# оплата WebMoney, оплата банковской карточкой и оплата по номеру телефона.

class Payments(ABC):
    @staticmethod
    @abstractmethod
    def payWebMoney():
        pass
    @staticmethod
    @abstractmethod
    def payCreditCard():
        pass
    @staticmethod
    @abstractmethod
    def payPhoneNumber():
        pass









def execute_application:
    pass



if __name__ == "__main__":
    execute_application()