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

# +
    def __is_fraction(self, other):
        if not isinstance(other,Fraction):
            raise TypeError(f"Невозможно выполнить сравнение "
                            f"между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __easy_fraction(self, other):
        if self.__denominator == other.__denominator:
            new_denominator = self.__denominator
            new_numerator = self.__numerator + other.__numerator
            return f"{new_numerator} / {new_denominator}"

    def __int_result(self):
        """
        Вернет целое число от деления числителя на знаменатель
        :param other:
        :return:
        """
        if self.__numerator % self.__denominator == 0:
            res = self.__numerator / self.__denominator
            return round(res)

    def __str__(self):
        return f"{self.__numerator} / {self.__denominator}"



def execute_application():
    pass






if __name__ == "__main__":
    execute_application()