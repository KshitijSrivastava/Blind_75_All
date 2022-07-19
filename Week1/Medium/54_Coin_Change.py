

#https://leetcode.com/problems/coin-change/

"""
Time Complexity: O(amount * len(coins)) stack space
Space Complexity: O( amount * len(coins) ) dictionary space
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        
        def recur(n, idx, amt):
            nonlocal dp
            if amt == 0:
                return 0
            elif idx == n or amt < 0:
                return float('inf')
            elif (amt, idx) in dp:
                return dp[ (amt, idx) ]
            
            #take
            coin_take = 1 + recur(n, idx, amt - coins[idx])
            
            coin_not_take = recur(n, idx + 1, amt)
            
            dp[ (amt, idx) ] = min(coin_take, coin_not_take)
            
            return dp[ (amt, idx) ]
        
        n = len(coins)
        value = recur(n, 0, amount)
        
        if value != float('inf'):
            return value
        return -1