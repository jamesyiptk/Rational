class Rational:
    def __init__(self, n, d=1):
        self.__numerator = n
        self.__denominator = d
        a = n
        b = d
        remainder = a % b
        while remainder != 0:
            a = b
            b = remainder
            remainder = a % b
        self.__numerator = n // b
        self.__denominator = d // b

    def __str__(self):
        return str(self.__numerator) + ' / ' + str(self.__denominator)

    def __float__(self):
        return float(self.__numerator) / self.__denominator

    def mul_rat(self, multiplier):
        top = self.__numerator * multiplier.__numerator
        bottom = self.__denominator * multiplier.__denominator
        return Rational(top, bottom)





print(float(Rational(3, 4)))