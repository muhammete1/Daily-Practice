"""
21.05.2022

İç İçe Fonksiyonlar
"""


def Calc(x):
    def square(x):
        return x ** 2

    def sqrt_(x):
        return x ** 0.5

    def fact(x):
        result = 1
        for x in range(1, x+1):
            result *= x
        return result

    sqre = square(x)
    sqrt = sqrt_(x)
    fct = fact(x)

    return f"square:{sqre}   sqrt:{sqrt}   fact:{fct}"

print(Calc(4))
