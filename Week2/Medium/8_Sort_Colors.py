"""
 z         t 
[2,0,2,1,1,0]
   z     t
[0,0,2,1,1,2]
     z   t
[0,0,2,1,1,2]
     
[0,0,1,1,2,2]


---------------------

[1,1,1,1,1]


"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        zero = 0
        two = n - 1
        
        zero_count = 0
        one_count = 0
        two_count =0
        
        for num in nums:
            if num == 0:
                zero_count += 1
            elif num == 1:
                one_count += 1
            else:
                two_count += 1
                
        idx = 0
        
        for i in range(zero_count):
            nums[idx] = 0
            idx += 1
            
        for i in range(one_count):
            nums[idx] = 1
            idx += 1
            
        for i in range(two_count):
            nums[idx] = 2
            idx += 1
            
        return nums