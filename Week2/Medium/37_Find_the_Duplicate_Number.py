
# https://leetcode.com/problems/find-the-duplicate-number/



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        while i < len(nums):
            if nums[i] != i + 1 and nums[ nums[i] - 1] != nums[i]:
                
                idx = nums[i]-1
                
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
                
        #print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]