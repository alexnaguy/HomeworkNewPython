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
class InternetPaymentService(Payments):
    @staticmethod
    def payWebMoney():
        print(f" Оплата производится через Электронные деньги")
    @staticmethod
    def payCreditCard():
        print(f"Оплата производится  по банковской карте")
    @staticmethod
    def payPhoneNumber():
        print(f"Оплата производится  по номеру телефона")


class TerminalPaymentService(ABC):

    def payWebMoney():
        print(f" Оплата производится через Электронные деньги")

    def payCreditCard():
        print(f"Оплата производится  по банковской карте")





def execute_application:
    pass



if __name__ == "__main__":
    execute_application()