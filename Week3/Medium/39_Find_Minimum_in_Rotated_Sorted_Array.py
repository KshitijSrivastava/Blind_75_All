"""

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

s     m     e
4,5,6,7,0,1,2


"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        start = 0
        end = n - 1
        
        res = -1
        
        while start <= end:
            mid = end - ((end - start) // 2)
            
            if nums[mid] >= nums[0]:
                res = mid
                start = mid + 1
            else:
                end = mid - 1
                
        return nums[ (res + 1) % n ]