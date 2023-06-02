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