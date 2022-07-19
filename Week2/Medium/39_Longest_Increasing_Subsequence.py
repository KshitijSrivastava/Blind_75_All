
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [1 for i in range(n)]
        
        for i in range(n):
            for j in range(i+1, n):
                
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i] + 1)
                    
        return max(dp)
                