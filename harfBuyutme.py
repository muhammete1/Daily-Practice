"""
5.05.2022

Ekranda okunan bir metinde "a" harflerini büyük yapan programı yazınız
"""
# 1.yol

txt = input("Please Enter a Text:")
txt2 = ""

for char in txt:
    if char != "a":
        txt2 += char
    else:
        txt2 += "A"
print(txt2)

# 2.yol

print(txt.replace("a", "A"))
