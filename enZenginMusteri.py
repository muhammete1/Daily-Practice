"""
15.12.2021

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
"""
accounts = [[1,5,5],[7,3],[3,5]]
def maximumWealth(accounts):
    sum = 0
    array1 = []
    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            sum += accounts[i][j]
        array1.append(sum)
        sum = 0
    return max(array1)
print(maximumWealth(accounts))

"""
Alternatif Çözüm:

def maximumWealth(accounts):
    for i in range(len(accounts)):
        accounts[i] = sum(accounts[i])
    return max(accounts)
print(maximumWealth(accounts))
"""