class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            profit_today = price - min_price
            max_profit = max(max_profit,profit_today)
            min_price = min(min_price,price)
        return max_profit
