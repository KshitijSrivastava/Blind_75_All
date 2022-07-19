
 #https://leetcode.com/problems/valid-anagram

class Solution:
    def make_dict(self, string):
        d = {}
        for char in string:
            if char not in d:
                d[char] = 0
            d[char] += 1
        return d 
            
    def isAnagram(self, s: str, t: str) -> bool:
        
        d_s = self.make_dict(s)
        d_t = self.make_dict(t)
        
        return d_s == d_t