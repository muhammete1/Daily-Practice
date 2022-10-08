"""
12.04.2022
"""


class persons:

    personCounter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        persons.personCounter += 1

    def show_info(self):    # Instance Methods
        return f"Name: {self.name}, Age:{self.age}"

    @classmethod
    def tell_person_counter(cls):
        return persons.personCounter


person1 = persons("Ahmet",19)
person2 = persons("Selim",20)

print(persons.personCounter)
print(persons.tell_person_counter())
