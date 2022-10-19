"""
format() yazım şekli ve f-string yazım şekilleri

"""

name = "Muhammet"
age = 22

print("ID information: {} {}".format(name,age))
print("ID information:",f"{name} {age}")


name1, age1 = "Kerim", 16
name2, age2 = "Selim", 18

print("{} and {} are".format(name1, name2), "{} and {} years old.".format(age1, age2))
