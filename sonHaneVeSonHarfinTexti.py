"""
                                        ███████╗██████╗ ███████╗███╗   ███╗
                                        ██╔════╝██╔══██╗██╔════╝████╗ ████║
                                        █████╗  ██████╔╝█████╗  ██╔████╔██║
                                        ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║
                                        ███████╗██████╔╝███████╗██║ ╚═╝ ██║
                                        ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝
"""
"""
Soru 1:
Verilen bir sayının son basamağını metin şeklinde döndüren fonksiyona ait kodları yazınız. 

Soru 2:
Verilen sayının rakamlarını ters sırayla yazdıran bir fonksiyona ait kodları yazınız. 
"""


class Solution:
    def convertTxt(self, num):
        list_ = ["Sıfır", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
        return list_[num % 10]

    def reverse_(self,num):
        numCnvrt = str(num)
        return int(numCnvrt[::-1])


num = int(input("Please enter your number:"))
sol = Solution()
print(sol.convertTxt(num))
print(sol.reverse_(num))