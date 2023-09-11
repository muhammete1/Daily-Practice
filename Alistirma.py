"""
11.06.2022
"""
list_ = [1,2,3,4]

polinom = lambda x, func: x + func(x)
print(polinom(2, lambda x: x**2))

#######################################

numbers = [23,45,11,22,18,109,178]

print(list(filter(lambda x: x % 2 == 0, numbers)))

#####################################################

words = ["air", "ice", "house", "table", "circle"]

print(list(filter(lambda word: "i" in word, words)))
print([word for word in words if "i" in word])

#####################################################

list2 = [1,10,99,23,41]

print(list(filter(lambda x: x > 20, list2)))

#############################################

bits = ["1111", "0000", "1010", "1100", "1110", "0001"]
const = 3
counter = 0
print([bit for bit in bits if "11" in bit])

#############################################


def control_str(x):
    if type(x) == str:
        return x


list3 = [1323, True, [1,23,4], "selam", False, "aga"]

print(list(filter(control_str, list3)))

###############################################


def control_palindrome(x):
    for i in x:
        if x[::-1] == x:
            return x


palindromeList = ["123", "121", "kazık", "11111", "11211", "ata"]

print(list(filter(control_palindrome, palindromeList)))

###############################################

plndromeLst = ["selam", "kelam", "0110", "küllük", "araba"]

print(list(filter(lambda plndrome: plndrome == plndrome[::-1], plndromeLst)))

###############################################

# print((lambda *args: args * args)(4, 5))




