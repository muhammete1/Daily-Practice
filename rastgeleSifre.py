"""
                                        ███████╗██████╗ ███████╗███╗   ███╗
                                        ██╔════╝██╔══██╗██╔════╝████╗ ████║
                                        █████╗  ██████╔╝█████╗  ██╔████╔██║
                                        ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║
                                        ███████╗██████╔╝███████╗██║ ╚═╝ ██║
                                        ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝
"""
import random

"""
Rastgele şifre oluşturucu
"""


class Solution:
    def __init__(self, SwordsList, BwordsList, numbers, specialExprs, charLen):
        self.SwordsList = SwordsList
        self.BwordsList = BwordsList
        self.numbers = numbers
        self.specialExprs = specialExprs
        self.charLen = charLen

    def createPassword(self):
        numList = [random.randint(0, 3)]
        wordList = [self.SwordsList, self.BwordsList, self.numbers, self.specialExprs]

        # Sword, Bword, number, specialExprs 'nin her birinden 1 karakter almak için döncek
        for j in range(3):  # 3 yazılmasının sebebi ilk başta rastgele bir değer alıyor
            # Rastgele gelen sayının aynı olmaması için
            while True:
                num1 = random.randint(0, 3)

                if num1 not in numList:
                    numList.append(num1)
                    break

        # Her biri farklı olan sayıları aldıktan sonra artık rastgele sayılar alınabilir
        for i in range(self.charLen-4):
            num2 = random.randint(0, 3)
            numList.append(num2)

        PASSWORD = ""
        # Üretilecek karakterler kadar dönücek
        for i in range(self.charLen):
            num3 = random.randint(0, len(wordList[numList[i]])-1)
            PASSWORD += wordList[numList[i]][num3]

        return PASSWORD


SwordsList = "qwertyuıopğüasdfghjklşizxcvbnmöç"
BwordsList = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
specialExprs = "*-,.!+-?"

while True:
    charLen = int(input("Please enter the character length:"))
    # 6 karakterden küçükse bir daha karakter uzunluğu sorsun
    if charLen >= 6:
        break
    else:
        print("Length of password is can be minimum 6 character")

sol = Solution(SwordsList, BwordsList, numbers, specialExprs, charLen)
print(sol.createPassword())
