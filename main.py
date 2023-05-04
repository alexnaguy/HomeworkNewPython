from abc import ABC, abstractmethod

class NotificationService(ABC):
    def send_message(self,message: str):
        pass


class EmailNotification(NotificationService):
    def send_message(self,message: str ):
        print(f"Сообщение {message} отправленно по электронной почте")


class MobileNotification(NotificationService):
    def send_message(self,message: str):
        print(f"Сообщение {message} отправленно на номер телефона")



def execute_application():
    email = EmailNotification()
    message = "За вами забронирвоан автомобиль"
    email.send_message(message)

    phone = MobileNotification()
    message = "За вами забронирвоан автомобиль"
    phone.send_message(message)

if __name__ == "__main__":
    execute_application()