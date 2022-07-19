
"""
 # https://leetcode.com/problems/combination-sum-iv/
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        dp = {}
        
        def recur(n, curr, target):
            nonlocal dp
            if curr == target:
                return 1
            elif curr > target:
                return 0
            elif curr in dp:
                return dp[curr]
            
            #take
            
            total = 0
            for num in nums:
            
                total += recur(n, curr + num, target)
                
            dp[curr] = total
            return total
        
        
        return recur(n, 0, target)