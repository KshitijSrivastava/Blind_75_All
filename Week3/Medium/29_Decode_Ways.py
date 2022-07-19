
# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        dp = {}
        
        def recur(idx, n):
            if idx == n:
                return 1
            elif idx in dp:
                return dp[idx]
            
            val1 = 0
            val2 = 0
            
            if idx == n-1:
                
                if int(s[idx]) >= 1 and int(s[idx]) <= 9:
                    val1 = recur(idx + 1, n)
                
            else:
                
                if int(s[idx]) >= 1 and int(s[idx]) <= 9:
                    val1 = recur(idx + 1, n)
                    
                if int(s[idx]) != 0 and int(s[idx: idx + 2]) >= 1 and int(s[idx:idx + 2]) <= 26:
                    val2 = recur(idx + 2, n)
                
            dp[idx] = val1 + val2
            return val1 + val2
        
        return recur(0, n)