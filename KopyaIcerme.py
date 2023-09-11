"""
3.13.2023

Given an integer array nums, return true if any value appears at least twice in the array, and return
false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
"""


class Solution:
    def ContaindDuplicate(self, nums):
        return len(nums) != len(set(nums))
    

nums = [2,14,18,22,22]
sol = Solution()
print(sol.ContaindDuplicate(nums))