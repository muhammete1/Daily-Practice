"""
                                        ███████╗██████╗ ███████╗███╗   ███╗
                                        ██╔════╝██╔══██╗██╔════╝████╗ ████║
                                        █████╗  ██████╔╝█████╗  ██╔████╔██║
                                        ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║
                                        ███████╗██████╔╝███████╗██║ ╚═╝ ██║
                                        ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝
"""
"""
Ad ve Soyadda belirli bir karakter uzunluğunu geçince * koyma

Örneğin : Muham*** Eb**
"""


class Solution:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def toApply(self):
        output = ""
        for i in range(len(self.name)):
            if i < 4:
                output += self.name[i]
            else:
                output += "*"
        output += " "
        for i in range(len(self.surname)):
            if i < 2:
                output += self.surname[i]
            else:
                output += "*"
        return output


name = input("Please enter your name:")
surname = input("Please enter your surname:")

CENSOR = Solution(name, surname)

print(CENSOR.toApply())

