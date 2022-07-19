
# https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def recur(count, n, curr, visited):
            if count >= n:
                output.append(curr[::])
                return
            
            
            for i in range(n):
                if visited[i] == False:
                    curr.append( nums[i] )
                    visited[i] = True
                    recur(count + 1, n, curr, visited)
                    visited[i] = False
                    curr.pop()
                    
        count = 0
        n = len(nums)
        curr = []
        visited = [False for i in range(n)]
        recur(count, n, curr, visited)
        return output