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
        return f"Описание товара: {self.__description}," \
               f" Количество: {self.__quantity}," \
               f" Цена: {self.__price}"

class CashRegister:
    def __init__(self):
        self.__retail_list = []

    def purchase_item(self, item: Retailltem):
        if not isinstance(item,Retailltem):
            raise TypeError (f"Недопустимый тип данных \'{item.__class__.__name__}\'. Ожидался \'RetailItem\'")
        return self.__retail_list.append(item)


    def get_total(self):
        summa = 0
        for item in self.__retail_list:
            summa += item.price * item.quantity
        return summa

    def show_iterns(self):
        if len(self.__retail_list) == 0:
            print("Товары отсутствуют")
        for item in self.__retail_list:
            print(item)

    def clear(self):
        self.__retail_list.clear()


def execute_application():
    retail = Retailltem("носки",4, 300)
    retail2 = Retailltem("худи",1, 5000)
    retail3 = Retailltem("пиджак", 3, 20000)

    cash_reg = CashRegister()
    cash_reg.purchase_item(retail)
    cash_reg.purchase_item(retail2)
    cash_reg.purchase_item(retail3)
    print(f"Данные товары: ")
    cash_reg.show_iterns()

    print(f"Суммарная стоимость товаров составляет: {cash_reg.get_total()} руб")

if __name__ =="__main__":
    execute_application()

