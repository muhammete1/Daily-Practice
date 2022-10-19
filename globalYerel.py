"""
9.06.2022

local, enclosing, global, built-in variables        ---> değişkenlerin kapsama alanına göre bakılma sırası
global      ---> "global" ifadesi kullanıldığında global'de yazılan değişkenin değerini fonksiyonlarda da değiştirilip
                 global değerin yerine almasını sağlar.

nonlocal    ---> "nonlocal" ifadesi iç içe fonksiyonlarda bir önceki değişkenin değerini değiştirmemizi sağlar.
"""
x = "global x"


def outer():
    x = "enclosing x"
    print(x)

    def inner():
        # x = "local x"
        print(x)
    inner()


outer()
print(x)

##############################
print("*"*20)

y = "global y"


def outer():
    global y
    y = 5
    print(y)


outer()
print(y)

##############################
print("*"*20)

z = "global z"


def outer():
    z = "enclosing z"
    print(z)

    def inner():
        nonlocal z
        z = 3

    inner()
    print(z)


outer()
print(z)
