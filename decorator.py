"""
26.05.2022

Decorator : @ ifadesinden sonra fonksiyon adı girilir. @ ifadesinin altındaki fonksiyonu, @ ifadesinden sonraki girilen
fonksiyon ifadesinin içine yazar.

Örneğin :

def sa(fonk):
    print(selam)

@sa
def as():
    print(aselam)
"""


def decorator(func):
    def wrapper():
        print("Condition before work")
        func()
        print("Condition after work")

    return wrapper


def func():
    print("The Function is working")


func2 = decorator(func)
func2()

print("*"*20)


def x(func):
    def wrapper():
        print("Condition before work")
        func()
        print("Condition after work")

    return wrapper

# @x        -> ifadesi decorater ifade eder. "x" ifadesi yukarıdaki fonksiyonun adıdır.
@x
def funci():
    print("The Function is working")


funci()

