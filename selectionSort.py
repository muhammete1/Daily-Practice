"""
18.07.2022

Selection Sort

Tanım :
Sıralama algoritması şu şekilde çalışıyor.Listede en küçük eleman bulunur. Bu elemean listenin ilk elemanı ile yer değiştirir.
Sonrasında liste bir sağa kayarak diğer elemanlar üzerinde en küçük değer bulunur ve aynı şekilde yer değiştirir.

"""


class Solution:
    def __init__(self, lst):
        self.lst = lst

    def slctSrt(self):

        for i in range(len(self.lst)-1):
            minValue = i
            for j in range(i+1, len(self.lst)):
                if self.lst[minValue] > self.lst[j]:
                    minValue = j
                    print(self.lst)
            self.lst[i], self.lst[minValue] = self.lst[minValue], self.lst[i]

        return self.lst


lst = [9,7,13,5,16]
sol = Solution(lst)
print(sol.slctSrt())
