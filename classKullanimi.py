"""
12.04.2022
"""


class employess:

    def __init__(self,a,b,c):
        self.name = a           # -> a = employess("Mehmet")
        self.surname = b        # -> b = employess("Altuğ")
        self.age = c            # -> c = employess(21)

    def show_info(self):
        print(f"Name:{self.name} , Surname:{self.surname} , Age:{self.age}")

            
worker1 = employess("Mehmet","Altuğ",21)
worker2 = employess("Sedat","Dursun",26)
worker1.show_info()
worker2.show_info()
