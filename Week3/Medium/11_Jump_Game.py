
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = 0
        
        i = 0
        while i < len(nums):
            
            if i > max_jump:
                return False
            
            if i == len(nums) - 1:
                return True
            
            max_jump = max(max_jump, i + nums[i])
            i += 1
            
        return max_jump >= n - 1