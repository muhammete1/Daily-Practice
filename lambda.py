"""
6.06.2022

lambda kullanımı : ismi olmayan fonksiyonlar oluşturmamızı sağlar.
"""

square = lambda param: param * param            # ----> square artık bir fonksiyon oluyor.
print(square(4))

addition = lambda x, y: x+y
print(addition(4,5))

# lambda ifadesini bir değere eşitlemeden de yazabiliriz.
print((lambda x, y, z: x * y + z)(4, 5, 6))


list_ = [("Ahmet",28), ("Kübra",19), ("Merve",18),("Berkan",20)]        # İsme göre sıralanması
list_.sort()
print(list_)


list2 = [("Ahmet",28), ("Kübra",19), ("Merve",18), ("Berkan",20)]        # Yaşa göre sıralanması
list2.sort(key=lambda x: x[1])
print(list2)

""" Yukarıdaki ile aşağıdaki aslında aynı fakat farklı yazım stilleridir. """

def showAge(x):
    return x[1]


list2.sort(key=showAge)                                                 # Yaşa göre sıralanması

