
# https://leetcode.com/problems/maximum-subarray/


class Solution:
     def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_sum = nums[0]
        summed = 0
        
        for i in range(0, len(nums)):
            summed = max(nums[i], summed + nums[i])
            
            max_sum = max(summed, max_sum)
        
        return max_sum