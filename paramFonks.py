"""
22.05.2022

Bir fonksiona parametre olarak fonksiyon verme
"""
list1 = [4,9,16]
list2 = [1,2,3,4,5,6]


def square(x):
    return x ** 2


def sqrt(x):
    return x ** 0.5


def map_(func, list_):
    result = []
    for i in list_:
        result.append(func(i))
    return result


print(map_(square, list2))
print(map_(sqrt, list1))
