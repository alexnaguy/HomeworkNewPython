from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_message(self,message: str, obj: str):
        pass


class EmailNotification(NotificationService):
    def send_message(self,message: str, email: str ):
        print(f"Сообщение {message} отправленно по электронной почте {email}")


class MobileNotification(NotificationService):
    def send_message(self,message: str, mobile: str):
        print(f"Сообщение {message} отправленно на номер телефона {mobile}")



def execute_application():
    email = EmailNotification()
    message = "За вами забронирвоан автомобиль"
    email.send_message(message, "nikut@yandex.ru")

    phone = MobileNotification()
    message = "За вами забронирвоан автомобиль"
    phone.send_message(message, "+79854567815")

if __name__ == "__main__":
    execute_application()