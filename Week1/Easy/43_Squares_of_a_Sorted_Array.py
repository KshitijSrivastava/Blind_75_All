
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        output = []
        
        n = len(nums)
        
        i = 0
        j = n - 1
        
        while i <= j:
            
            s = nums[i] * nums[i]
            e = nums[j] * nums[j]
            
            if s > e:
                output.append(s)
                i += 1
            else:
                output.append(e)
                j -= 1
        return output[::-1]