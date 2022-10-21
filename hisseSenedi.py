"""
4.02.2022

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def maxProfit(prices):
    profit = []
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                profit.append(prices[j] - prices[i])
            else:
                break
    if not profit:
        return 0
    else:
        return max(profit)

prices = [7,2,10,1,5,3,6,4]
print(maxProfit(prices))