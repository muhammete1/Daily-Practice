"""
30.12.2021

Çocukların sahip olduğu bir şeker miktarı vardır. Bu çocuklara extra şeker verildiğinde dair, en fazla şekere sahip
çocuktan az şekeri bulunuyorsa false döndürürülecektir.
"""
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        most = max(candies)
        boolList = []
        for i in candies:
            i += extraCandies
            if most <= i:
                boolList.append(True)
            else:
                boolList.append(False)
        return boolList

candies = [2, 3, 5, 1, 3]
extraCandies = 2
solution = Solution()
print(solution.kidsWithCandies(candies, extraCandies))
