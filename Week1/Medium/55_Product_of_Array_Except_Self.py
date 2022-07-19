"""
[1,2,3,4]

[1,2,6,12]

[24,24,12,4] right

# https://leetcode.com/problems/product-of-array-except-self/


"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        output = []
        
        left = []
        right = []
        
        curr = 1
        for num in nums:
            curr = curr * num
            left.append(curr)
            
        curr = 1
        for i in range(n-1, -1, -1):
            num = nums[i]
            curr = curr * nums[i]
            right.append(curr)
            
        right = right[::-1]
        
        for i in range(n):
            if i == 0:
                output.append( right[i+1] )
            elif i == n-1:
                output.append( left[i-1] )
            else:
                output.append( left[i-1]  * right[i+1] )
            
        return output