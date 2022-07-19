

# https://leetcode.com/problems/contiguous-array/


"""
original [0,1,0]

change [-1,1,-1]
prefix [0, -1, 0, -1]
        -1  0   1   2
        
[1,1,1,1,0,0,0,0,1,1,0]
[0,1,2,3,4,-3,-2,-1,0,1,2,-1 ]

[1,1,1,1,1,0,0,0,1,1,1,1,1]
[1,2,3,4,5,4,3,2,3,4,5,6,7]
[0,1,2,3,4,5,6,7,8,9,10,11,12]
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        d = { 0: -1 }
        
        
        max_length = 0
        curr_sum = 0
        for idx, num in enumerate(nums):
            
            if num == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
                
            if curr_sum in d:
                index = d[curr_sum]
                length = idx - index
                
                max_length = max(max_length, length)
            else:
                d[curr_sum] = idx
                
        return max_length