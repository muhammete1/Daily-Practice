"""
                                        ███████╗██████╗ ███████╗███╗   ███╗
                                        ██╔════╝██╔══██╗██╔════╝████╗ ████║
                                        █████╗  ██████╔╝█████╗  ██╔████╔██║
                                        ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║
                                        ███████╗██████╔╝███████╗██║ ╚═╝ ██║
                                        ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝
"""
"""
Boyutu kullanıcıdan alınan kare matris oluşturan ve bunları konsola formatlı şekilde yazdıran program için gerekli kodları yazınız
"""
import random


class Solution:
    def __init__(self, row, column, list_):
        self.row = row
        self.column = column
        self.list_ = list_

    def createMatrix(self):
        counter = 0
        for i in range(row):
            for j in range(column):
                if counter == 0:
                    print("[",list_[counter], "\t", end="")
                elif list_[counter] == list_[-1]:
                    print(list_[counter], "]", "\t", end="")
                else:
                    print(list_[counter], "\t", end="")
                counter += 1
            print("\n")


row = int(input("Please enter your number of row:"))
column = int(input("Please enter your number of column:"))
list_ = []
for i in range(column + row):
    num = random.randint(0,100)
    list_.append(num)


sol = Solution(row, column, list_)
sol.createMatrix()
