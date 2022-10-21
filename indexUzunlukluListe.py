"""
20.01.2022

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
"""
class Solution:
    def a(nums):
        output = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                output.append(nums[i+1])
        return output


sol = Solution
nums = [1, 2, 3, 4]
print(sol.a(nums))
