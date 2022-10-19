"""
7.07.2022

filter() fonksyinou kullanımı : İçine bir fonksiyon ve bir liste alır. Fonksiyondan true olarak dönen değerler geri döndürülür
"""
words = ["car", "mouse", "choice", "camel", "water", "microscope"]


def Same(word):
    if word.startswith("c"):
        return True
    return False


print("Same Startswith:", list(filter(Same, words)))


# Yeni Örnek
numbers = [23,45,11,22,18,109,178]

print("Numbers dividing by two:", list(filter(lambda number: number % 2 == 0, numbers)))


# Yeni Örnek
words = ["air", "ice", "house", "table", "circle"]

print("Find Character:", list(filter(lambda word: "i" in word, words)))


# Yeni Örnek
words = ["ana", "iki", "sekiz"]

print("Palindrome:", list(filter(lambda word: word == word[::-1], words)))
