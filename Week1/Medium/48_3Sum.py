# https://leetcode.com/problems/3sum/

"""
Time Complexity: O(N * N)
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        nums.sort()
        
        s = set()
        output = []
        
        for i in range(n):
            
            j = i + 1
            k = n - 1
            
            while j < k and j > i and k > i:
                
                if nums[i] + nums[j] + nums[k] == 0:
                    
                    if (nums[i], nums[j], nums[k]) not in s:
                        s.add( (nums[i], nums[j], nums[k]) )
                        output.append( [ nums[i], nums[j], nums[k] ] )
                    j += 1
                
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    
                else:
                    k -= 1
                    
        return output