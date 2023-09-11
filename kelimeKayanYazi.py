"""
                                        ███████╗██████╗ ███████╗███╗   ███╗
                                        ██╔════╝██╔══██╗██╔════╝████╗ ████║
                                        █████╗  ██████╔╝█████╗  ██╔████╔██║
                                        ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╔╝██║
                                        ███████╗██████╔╝███████╗██║ ╚═╝ ██║
                                        ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝
"""
"""
Yazılan adın alfabede karşılığı gelene kadar devam etmesi
"""
import time


class Solution:
    def __init__(self, name):
        self.name = name

    def Output(self):
        alphabate = " abcçdefgğhıijklmnoöprsştuüvyzwq"
        temp = ""
        for i in range(len(self.name)):
            for j in range(len(alphabate)):
                if self.name[i] != alphabate[j]:
                    print(temp + alphabate[j])
                    time.sleep(0.5)
                else:
                    print(temp + alphabate[j])
                    print(end="")
                    temp += alphabate[j]
                    break


name = input("Please enter your name:")

sol = Solution(name)
sol.Output()