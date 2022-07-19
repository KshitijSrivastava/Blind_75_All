

# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count_zeros = 0
        for num in nums:
            if num == 0:
                count_zeros += 1
                
        n = len(nums)
                
        idx = 0
        i = 0
        while i < n:
            if nums[i] == 0:
                i += 1
                continue
                
            nums[idx] = nums[i]
            idx += 1
            i += 1
            
        for i in range(count_zeros):
            nums[n-1-i] = 0
            
        