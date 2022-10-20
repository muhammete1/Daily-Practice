"""
4.05.2022

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""


def search(nums, target):
    if target in nums:
        result = nums.index(target)
    return result


nums = [-1,0,2,4,5]
target = 4
print(search(nums, target))
