class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)          # best day to buy so far
            profit = price - min_price                 # sell today
            max_profit = max(max_profit, profit)

        return max_profit