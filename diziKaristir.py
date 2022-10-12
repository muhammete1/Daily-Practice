"""
15.12.2021

[x1,x2,...,xn,y1,y2,...,yn] formdaki öğelerden oluşan dizi göz önüne alındığında
Diziyi biçiminde döndürün.[x1,y1,x2,y2,...,xn,yn]

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
"""
nums = [2,5,1,3,4,7]
n = 3

def shuffle(nums, n):
    array1 = []
    array2 = []
    for i in range(n):
        array1.append(nums[i])
    for i in range(n):
        array2.append(array1[i])
        array2.append(nums[i+n])

    return array2
print(shuffle(nums, n))