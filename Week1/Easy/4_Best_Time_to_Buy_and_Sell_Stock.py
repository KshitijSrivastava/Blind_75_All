
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        mini_cost = float('inf')
        
        for p in prices:
            
            mini_cost = min(mini_cost, p)
            
            profit = p - mini_cost
            
            max_profit = max(max_profit, profit)
            
        return max_profit