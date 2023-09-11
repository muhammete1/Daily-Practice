"""
18.07.2022

Kullanıcıdan input alıcaz. Girdiğimiz string değeleri içerisinde kullandığımız harfler 1'den fazla
ise onları kullanmıcaz.
Örneğin :
Input : "araba kullanmaya gidicez"
Output : "arb kulnmy gdcz"
"""


class Solution:
    def __init__(self, sentence):
        self.sentence = sentence

    def dontRepeat(self):
        words = {}
        sntnce = ""
        for i in self.sentence:
            if i in words:
                words[f"{i}"] += 1
            elif i == " ":
                sntnce += i
            else:
                words[f"{i}"] = 1
                sntnce += i

        print(words)
        print(sntnce)


sentence = input("Please Enter Your Sentence:")
sol = Solution(sentence)
sol.dontRepeat()

