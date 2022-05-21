"""
Verilen sayıya göre ay tahmini yapan kodu yazınız.
"""
import random


class Prediction:

    moons = {1:"Ocak", 2:"Şubat", 3:"Mart", 4:"Nisan", 5:"Mayıs", 6:"Haziran", 7:"Temmuz", 8:"Ağustos", 9:"Eylül",
             10:"Ekim", 11:"Kasım", 12:"Aralık"}

    def guess(self):

        while True:
            numb = random.randint(1, 12)
            print(numb)
            predMonth = input("Please enter your Prediction:")

            while True:
                if self.moons[numb] == predMonth:
                    print("Well Done")
                    break
                else:
                    print("Wrong Prediction!")
                    predMonth = input("Please enter your Prediction:")


prediction1 = Prediction()
prediction1.guess()





