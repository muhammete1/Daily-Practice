"""
27.052022

Sayıyının Türkçe Karşılığının Metne Dönüştürme

0 < num < 100
"""


class Solution:
    def Convert(self, num):
        onesDigit = {0: "Sıfır", 1: "Bir", 2: "İki", 3: "Üç", 4: "Dört", 5: "Beş", 6: "Altı", 7: "Yedi",
                     8: "Sekiz", 9: "Dokuz"}
        tensDigit = {1: "On", 2: "Yirmi", 3: "Otuz", 4: "Kırk", 5: "Elli", 6: "Atmış", 7: "Yetmiş",
                     8: "Seksen",9: "Doksan"}

        numOnes = num % 10
        if num >= 10:
            return f"{tensDigit[(num - numOnes) / 10]} {onesDigit[numOnes]}"
        else:
            return f"{onesDigit[num]}"


num = int(input("Please Enter your number:"))
sol = Solution()
print(sol.Convert(num))
