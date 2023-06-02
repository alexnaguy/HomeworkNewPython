class Number:
    def __init__(self, value, base = None):
        self.__value = value
        self.__base = base


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        self.__base = base


class Calculator:
    def __init__(self,number: Number):
        self.__number = number

    #Методы пеобразвания в СС

    # Из десятичной в двоичную

    def calc_bin(self):
        result = bin(self.__number.value)
        return result
    # в восьмеричную

    def calc_oct(self):
        result = oct(self.__number.value)
        return result


    def calc_hex(self):
        result = hex(self.__number.value)
        return result

# Из СС любой в десятичную
    def calc_int(self):
        result = int(self.__number.value, self.__number.base)
        return result
