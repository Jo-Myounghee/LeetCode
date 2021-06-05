class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            min_val = min(min_val, prices[i])
            profit = max(profit, prices[i]-min_val)
        
        return profit