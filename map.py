"""
7.06.2022

map() fonksiyonu kullanımı : İçerisine bir fonksiyon ve liste yazılır. Fonksiyonun içine listeyi atarak işlemler yapar.
"""


def square(a):
    return a ** 2


list_ = [1,2,3,4,5]

list1 = list(map(square, list_))
print("list:", list1)

list1 = tuple((map(square, list_)))
print("tuple:", list1)

# Farklı bir yazım stili
print(list(map(lambda value: value * value, list_)))


# Yeni Örnek
products = [["Shoes", 500], ["Clothes", 300], ["Glasses", 150], ["Pants", 200]]


def discount(x):
    product, price = x[0], x[1]
    return [product, price*(9/10)]


print(list(map(discount, products)))


# Yeni Örnek
names = ["MURat", "SeDa", "cAhiT", "tamER"]

print(list(map(lambda name: name.lower(), names)))
