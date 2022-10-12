"""
11.12.2021

Bir dizi verildi. Bu dizinin çalışan toplamını runningSum[i] = sum(nums[0]…nums[i]) olarak tanımlıyoruz.
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""
nums = [1, 5, 7, 4, 5]
def runningSum(nums):
    newArray = []
    counter = 0
    for i in range(1, len(nums)+1):
        counter += nums[i-1]
        newArray.append(counter)
    return newArray
print(runningSum(nums))