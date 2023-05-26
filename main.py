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


# Сравнение дробей
    def __hash__(self):
        return hash(self.__numerator, self.__denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator *  other.denominator <= other.numerator *  self.denominator

    def __gt__(self, other):
        return self.numerator *  other.denominator > other.numerator *  self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator


# +
    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.__is_fraction(other)
        new_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        self.__easy_fraction(other)
        new_denominator = self.__denominator * other.__denominator
        self.__int_result()
        if new_numerator % new_denominator == 0:
            res = new_numerator / new_denominator
            return round(res)
        return (f"{new_numerator} / {new_denominator}")


#-
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.__is_fraction(other)
        new_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        if new_numerator % new_denominator == 0:
            res = new_numerator / new_denominator
            return round(res)
        return (f"{new_numerator} / {new_denominator}")
# *
    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.__is_fraction(other)
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        self.__int_result()
        if new_numerator % new_denominator == 0:
            res = new_numerator / new_denominator
            return round(res)
        return (f"{new_numerator} / {new_denominator}")


# /
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        self.__is_fraction(other)
        new_numerator = self.__numerator * other.__denominator
        self.__easy_fraction(other)
        new_denominator = self.__denominator * other.__numerator
        self.__int_result()
        if new_numerator % new_denominator == 0:
            res = new_numerator / new_denominator
            return round(res)
        return (f"{new_numerator} / {new_denominator}")







def execute_application():
    pass






if __name__ == "__main__":
    execute_application()