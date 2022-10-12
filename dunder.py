"""
21.05.2022

Dunder Methods : "object.__funcName()__" olan ifadelere denir.

['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__',
 '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__',
  '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__',
   '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__',
    '__rdivmod__', '__reduce__',]

__sub__ for subtraction(-)
__mul__ for multiplication(*)
__truediv__ for division(/)
__eq__ for equality (==)
__lt__ for less than(<)
__gt__ for greater than(>)
__le__ for less than or equal to (≤)
__ge__ for greater than or equal to (≥)
"""

print(1 + 3)
print(int.__add__(1, 3))

print("Selim" + "Aslı")
print(str.__add__("Selim", "Aslı"))

print([1,2,3] + [4,5,7])
print(list.__add__([1,2,3], [4,5,7]))

print("*"*20)


class MyList(list):
    def __add__(self, other):
        if len(self) != len(other):     # self ile other list1 ve list2'nin yerini tutuyor
            return "These lists are not collectible."
        else:
            result = MyList()
            for i in range(len(self)):
                result.append(self[i] + other[i])
        return result

    def __sub__(self, other):
        if len(self) != len(other):     # self ile other list1 ve list2'nin yerini tutuyor
            return "These lists are not removable."
        else:
            result = MyList()
            for i in range(len(self)):
                result.append(self[i] - other[i])
        return result

    def __eq__(self, other):
        if sum(self) == sum(other):
            return True
        else:
            return False


list1 = MyList([1,2,3])
list2 = MyList([4,5,6])
print(f"list1:{list1}    list2:{list2}")
print("Add:", list1 + list2)
print("Sub:", list1 - list2)
print("Equal:", list1 == list2)
