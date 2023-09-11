"""
18.07.2022

Selection Sort

Tanım :
Sıralama algoritması şu şekilde çalışıyor.Listede en küçük eleman bulunur. Bu elemean listenin ilk elemanı ile yer değiştirir.
Sonrasında liste bir sağa kayarak diğer elemanlar üzerinde en küçük değer bulunur ve aynı şekilde yer değiştirir.
"""


class Example:
    def __init__(self, list_):
        self.lst = list_

    def slctnSort(self):
        newList = []
        for i in range(len(self.lst)):
            min_ = min(self.lst)
            newList.append(min_)
            self.lst.remove(min(self.lst))

        return newList


lst = [9,7,13,5,16]
print("First view of list:", lst)
algorithm1 = Example(lst)
print("Last view of list:", algorithm1.slctnSort())
