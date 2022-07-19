
"""
# https://leetcode.com/problems/subarray-sum-equals-k/

[1,1,1]

0: 1
-----
0:1
1:1
------
0:1
1:1
2:1
-------
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total = 0
        
        curr_sum = 0
         
        prefix_sum = { 0: 1 }
        
        for num in nums:
            curr_sum += num
            
            if curr_sum - k in prefix_sum:
                total += prefix_sum[ curr_sum - k ]
                
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum] = 0
            prefix_sum[curr_sum] += 1
            
        return total