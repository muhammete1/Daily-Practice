"""
3.13.2023

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
"""


class Solution:
    def singleNumber(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]

nums = [4,1,2,1,2]
sol = Solution()
print(sol.singleNumber(nums))
