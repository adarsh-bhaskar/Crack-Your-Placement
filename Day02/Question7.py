# Leetcode 121

from typing import List

def maxProfit(prices: List[int]) -> int:
    min_profit = prices[0]
    max_profit = 0

    for price in prices:
        profit = price - min_profit
        max_profit = max(max_profit, profit)
        min_profit = min(min_profit, price)
    
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))