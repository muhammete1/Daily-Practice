"""
7.01.2022

Dizi göz önüne alındığında, her biri için dizideki kaç sayının ondan daha küçük olduğunu öğrenin.
Yani, her biri için geçerli sayısını saymanız gerekir.Yanıtı bir dizide döndürün.
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""

class Soultion:
    def smallerNumbersThanCurrent(self):
        counter = 0
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j] and i != j:
                   counter += 1
            output.append(counter)
            counter = 0
        return output


sl = Soultion()
nums = [8, 1, 2, 2, 3]

sl.smallerNumbersThanCurrent()
