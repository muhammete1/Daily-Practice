"""
                                        ███████╗██████╗ ███████╗███╗   ███╗
                                        ██╔════╝██╔══██╗██╔════╝████╗ ████║
                                        █████╗  ██████╔╝█████╗  ██╔████╔██║
                                        ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║
                                        ███████╗██████╔╝███████╗██║ ╚═╝ ██║
                                        ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝
"""
"""
Kullanıcıdan alınan 2 tamsayının tüm varyasyonlarını yazdıran kodları yazınız. 
"""


class Solution:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def variation(self):
        for i in range(self.num1+1):
            for j in range(self.num2+1):
                print([i, j], end=" ")


num1 = int(input("Please enter your number:"))
num2 = int(input("Please enter your number:"))

sol = Solution(num1, num2)
sol.variation()

