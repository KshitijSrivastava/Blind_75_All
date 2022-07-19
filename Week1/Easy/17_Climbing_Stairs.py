
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        
        def recur(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in dp:
                return dp[n]
        
            dp[n] =  recur(n-1) + recur(n-2)
            return dp[n]
        return recur(n)