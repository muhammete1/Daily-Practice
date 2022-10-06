"""
18.04.2022

"*args" ifadesinin kullanımı : Fonksiyona girceğimiz parametre sayısını bilmiyorsak *args parametresini kullanırız.
*args ' lar tuple ifadelerdir.

Bilgi : * ifadesinden sonra herhangi bir şey yazabiliriz. Örneğin : *yks

"**kwargs" ifadesinin kullanımı : Fonksiyona istediğimiz kadar keyword argument girmemizi sağlar.
**kwargs ' lar dictionary ifadelerdir.

Bilgi : ** ifadesinden sonra herhangi bir şey yazabiliriz. Örneğin : **bilgiler
"""


def Sum(*args):

    print([arg for arg in args])

    sum_ = 0
    for arg in args:
        sum_ += arg
    return sum_


print(Sum(2, 3, 5, 1))


def medium(*values):  # Ortalama

    return sum(values) / len(values)


print(medium(6, 8, 9))

print("*****************")


def hi(message, *args, **kwargs):
    print(message)
    print("********")
    print([arg for arg in args])
    print("**************")
    for k,v in kwargs.items():
        print(k,v)


hi("Hello",1,2,3,4,5,6,name="Mehmet",surname="Karahanlı")
