"""
5.05.2022

Metinsel bir ifade de harflerin kaç defa yazıldığını gösteren program
"""

txt = input("Please Enter a Text:")
dictionary = dict()

for char in txt:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1
for char, counter in dictionary.items():
    print(char, counter)
