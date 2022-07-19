
# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = {}
        
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
            
        
        count = 0
        single = False
        for k, v in d.items():
            
            if v % 2 == 0:
                count += (v)
            else:
                count += ( v - 1 )
                single = True
                
        if single:
            return 1 + count
        return count