from abc import ABC, abstractmethod
class NotificationService:
    pass
class NotificationService(ABC):
    def send_message(self,message: str):
        pass


class EmailNotification(NotificationService):
    pass
    def send_message(self,message: str ):
        print(f"Сообщение {message} отправленно по электронной почте")


class MobileNotification(NotificationService):
    pass
    def send_message(self,message: str):
        print(f"Сообщение {message} отправленно на номер телефона")



def execute_application():
    pass

if __name__ == "__main__":
    execute_application()