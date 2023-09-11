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

        for i in range(len(self.lst)-1):
            min_ = self.lst[i]
            for j in range(i+1, len(self.lst)):
                if min_ > self.lst[j]:
                    min_ = self.lst[j]
                    self.lst[i], self.lst[j] = min_, self.lst[i]
            print(self.lst)

        return self.lst


lst = [9,7,13,5,16]
print("First view of list:", lst)
algorithm1 = Example(lst)
print("Last view of list:", algorithm1.slctnSort())
