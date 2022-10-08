"""
9.01.2022

Size aynı uzunluktabir dize ve tamsayı dizisi verilir.
Dize, konumdaki karakterin karıştırılmış dizeye taşınacağı şekilde karıştırılır.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
"""


class Solution:
    def restoreString(self):
        a = list(s)
        for i in range(len(s)):
            a[indices[i]] = s[i]
        print("".join(a))
sol = Solution()

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
sol.restoreString()
