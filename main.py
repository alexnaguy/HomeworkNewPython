import math
class Fraction:

    def __init__(self,numerator: int, denominator:int):
        self.__nod = math.gcd(numerator,denominator)
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator
    @property
    def denominator(self):
        return self.__denominator





def execute_application():
    pass






if __name__ == "__main__":
    execute_application()