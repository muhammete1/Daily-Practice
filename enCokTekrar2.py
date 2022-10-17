"""
27.05.2022

lst içindeki [[i] ,[lst.count(i)]]
"""


class Solution:
    def result(self, lst):
        maxVal = []
        counter = 0
        for i in lst:
            print([[i], [lst.count(i)]])
            maxVal.append(lst.count(i))
        for i in lst:
            if lst.count(i) == max(maxVal):
                counter += 1
                if counter == max(maxVal):
                    print(i)


sol = Solution()
list_ = [1,2,2,3,2,6,1,2,2,3,2,6,1,2,2,3,2,6,7,8,4,5,7,8,8,7]
list2 = [1,2,1,3,4,5,6,6,8,1,6]
sol.result(list_)
