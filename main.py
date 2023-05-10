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

#Задание 2
# Рассмотрим принцип инверсии зависимостей. Исправьте следующий код таким
# # образом, чтобы классы и верхних, и нижних уровней зависели от одних и тех же
# # абстракций, а не от конкретных реализаций.

class Authentication:
    @abstractmethod
    def doAauthentication(self, login: str):
        pass

class AnonymousAuthentication:
    def doAauthentication(self,login: str):
        print(f"Анонимная регистрация пользователя {login}")

class GithubAuthentication:
    def doAuthentication(self,login: str):
        print(f"Регистрация на GitHub пользователя {login}")

class FacebookAuthentication:
    def doAuthentication(self,login: str):
        print(f"Регистрация на Faebook пользователя {login}")

class Permissions:
    def __init__(self, auth: AnonymousAuthentication):
        self.__auth = copy(auth)

    def getPermissions(self, login: str):
        self.__auth.doAauthentication(login)

def execute_application:


    InternetPaymentService.payPhoneNumber()
    TerminalPaymentService.payCreditCard()

if __name__ == "__main__":
    execute_application()