
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        
        mask = 1
        for i in range(33):
            
            if mask & n != 0:
                count += 1
            mask = mask << 1
            
            #print(mask)
        return count