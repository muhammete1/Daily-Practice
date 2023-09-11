"""
8.12.2021

Bir dizideki belirli bir konumdaki bir elemanın iki komşusundan daha büyük olup olmadığını kontrol eden bir
fonksiyona ait kodları yazın
"""
def neighbor(list1, index):
    counter = 0;
    for i in list1:
        if index == i:
            if list1[counter-1] < list1[counter] and list1[counter+1] < list1[counter]:
                print("Your select number biggest")
            else: print("Your select number not biggest")
        elif len(list1) == counter:
            print("Invalid Index!")
            break
        counter += 1

list1 = [1,82,12,57,77,3,5]
index = int(input("Please select number from list1:"))
neighbor(list1, index)