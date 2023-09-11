"""
7.10.2022
re Modülü Fonksiyonları
"""
import re


def find(process):
    obj = re.search("go", process)
    print(obj.span())
    print(process[obj.span()[0] : obj.span()[1]])


process = "That was great. We go outside tomorrow. Okay?"
find(process)
