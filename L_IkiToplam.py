"""
Bir dizi tamsayı ve bir tamsayı verildiğinde, iki sayının dizinlerini hedefe topladıkları şekilde döndürün.
Her girişin tam olarak bir çözümüolduğunu varsayabilirsiniz ve aynı öğeyi iki kez kullanmayabilirsiniz.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

list1 = [2,1,9,4,4,56,90,3]
target = 8

def TwoSum(list2 , target):
    sayac = 0
    sayac2 = 0
    for i in range(len(list2)):
        if (sayac2 == 0):
            for j in range(1, len(list2)):
                if (list2[i] + list2[j + sayac] == target):
                    return [i, j + sayac]
        else:
            for j in range(1, len(list2) - sayac):
                if (list2[i] + list2[j + sayac] == target):
                    return [i, j + sayac]
        sayac +=1
        sayac2 = 1


print(TwoSum(list1 , target))

#def TwoSum2(list2 , target):
#    k = 1
#    while True:
#        for i in range(len(list2)):
#            if (list2[i] + list2[k] == target):
#                return [i, k]
#        k +=1
#
#print(TwoSum2(list1 , target))