

# https://leetcode.com/problems/subsets/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def recur(idx, n, curr):
            if idx == n:
                output.append( curr[::] )
                return
            
            #take
            curr.append( nums[idx] )
            recur(idx + 1, n, curr)
            curr.pop()
            
            #no take
            recur(idx + 1, n, curr)
            
        idx = 0
        curr = []
        n = len(nums)
        recur(idx, n, curr)
        return output