"""
19.05.2022

Listede en çok tekrar eden sayıyı bulma kodu
"""


class Solution:
    def result(self, lst):
        dc = {}
        for i in lst:
            if str(i) in dc:
                dc[f"{i}"] += 1
            else:
                dc[f"{i}"] = 1


        maxVal = 0
        maxKey = ""

        for i in dc:
            if maxVal < dc[i]:
                maxVal = dc[i]
                maxKey = i
        print(dc)
        print(maxKey)
        print(maxVal)


sol = Solution()
list_ = [1,2,2,3,2,6,1,2,2,3,2,6,1,2,2,3,2,6,7,8,4,5,7,8,8,7]
list2 = [1,2,1,3,4,5,6,6,8,1,6]
sol.result(list2)
