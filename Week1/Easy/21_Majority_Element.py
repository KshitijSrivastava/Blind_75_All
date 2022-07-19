

# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        stack = []
        
        for num in nums:
            
            if len(stack) == 0:
                stack.append(num)
            elif stack[-1] != num:
                stack.pop()
            else:
                stack.append(num)
                
        return stack[-1]