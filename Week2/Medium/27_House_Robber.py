
# https://leetcode.com/problems/house-robber/



class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = {}
        
        def rob_recur(nums, idx):
            if idx >= n:
                return 0
            elif idx in dp:
                return dp[idx]
            
            #rob this house
            value1 = nums[idx] + rob_recur(nums, idx + 2)
            
            #not rob this house
            value2 = rob_recur(nums, idx + 1)
            
            dp[idx] = max(value1, value2)
            return dp[idx]
        
        return rob_recur(nums, 0)