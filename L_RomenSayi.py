"""
Girilen sayının romen karşılığını döndürün.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
"""
list1 = {"I":1 ,"V":5 , "X":10 ,"L":50 , "C":100 , "D":500 , "M":1000}
print(list1)
write = input("Enter Roman numerals:")

l1 = list(list1.keys())
l2 = list(list1.values())
list2 = []

#Yazdığımız write'ın değerini listeye atıp değerlerini teker teker aldım
for i in range(len(write)):
    list2.append(write[i])
print(list2)

sum1=0
counter = 0
for a in range(1):
    for j in range(len(write)):  #write ile l1 değerleri eşleşiyorsa values değerini vermesini sağlıcaz
        for k in range(len(l1)):
            if (list2[j] == l1[k]):
                list2[j] = l2[k]
                print(list2)
    while (counter != len(write)): #write'ın yan yana değerlerini karşılaştırıyoruz
            try:
                if (list2[counter] < list2[counter + 1]):
                    if (list2[counter] > list2[counter + 1]):
                        sum1 += list2[counter]
                    else:
                        sum1 += list2[counter + 1] - list2[counter]
                        counter += 1
                else:
                    if (list2[counter] >= list2[counter + 1]):
                        sum1 += list2[counter]
                    else:
                        sum1 += list2[counter + 1] - list2[counter]
                counter+=1
            except IndexError:
                sum1 += list2[-1]
                break
print("Toplam:" , sum1)









