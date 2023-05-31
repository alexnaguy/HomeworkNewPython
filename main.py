class Retailltem:

    def __init__(self,description: str, quantity: int, price: float):
        self.__description = description
        self.__quantity = quantity
        self.__price = price

    @staticmethod
    def __is_description(item):
        if not isinstance(item, str):
            raise TypeError (f"Не верный тип данных: {item.__class__.__name__}"
                            f"ожидался 'str'")
        return item

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = self.__is_description(description)


    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self,quantity):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return f"Описание товара: {self.__description}, Количество: {self.__quantity}, Цена:{self.__price}"