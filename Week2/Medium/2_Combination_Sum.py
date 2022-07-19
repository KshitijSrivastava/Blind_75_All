
# https://leetcode.com/problems/combination-sum/


import copy 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        def recur(idx, n, curr_sum, curr):
            nonlocal output
            if idx >= n:
                return 
            elif curr_sum == target:
                print(curr)
                output.append( curr.copy() )
                return
            elif curr_sum > target:
                return
            
            #take the element
            curr.append( candidates[idx] )
            recur(idx, n, curr_sum + candidates[idx], curr )
            curr.pop()
            
            #not take the element
            recur(idx + 1, n, curr_sum, curr)
            
        idx = 0
        n = len(candidates)
        curr_sum = 0
        curr = []
        recur(idx, n, curr_sum, curr)
        return output