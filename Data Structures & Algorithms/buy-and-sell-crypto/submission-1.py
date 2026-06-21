class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    temp = profit
                    max_profit = max(max_profit, profit)
                
        return max_profit

