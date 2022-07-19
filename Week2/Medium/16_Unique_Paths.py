

# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        
        def recur(i, j, m, n):
            if i == m - 1 and j == n - 1:
                return 1
            elif i < 0 or i >= m or j < 0 or j >= n:
                return 0
            elif (i,j) in dp:
                return dp[ (i,j) ]
            
            down = recur(i+1, j, m, n)
            right = recur(i, j+1, m, n)
            
            dp[ (i,j) ] = down + right
            
            return down + right
        
        
        return recur(0,0, m, n)