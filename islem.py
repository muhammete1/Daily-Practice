"""
9.01.2022

Verilen sayının rakamlarının çarpımı ile toplamının farkını alan kodu yazınız.

Input = 234
Explanation = (2 * 3 * 4) - (2 + 3 + 4)
Output = 15
"""


class Solution:
    def distance(self, n):
        multi = 1
        sum1 = 0
        for i in range(len(str(n))):
            multi *= int(str(n)[i])
            sum1 += int(str(n)[i])
        return multi - sum1


n = 234
sl = Solution()

print(sl.distance(n))
