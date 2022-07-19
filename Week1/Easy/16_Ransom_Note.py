

# https://leetcode.com/problems/ransom-note/

class Solution:
    def construct_dict(self, string):
        d = {}
        for char in string:
            if char not in d:
                d[char] = 0
            d[char] += 1
        return d
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        d_r = self.construct_dict(ransomNote)
        d_m = self.construct_dict(magazine)
        
        for k, v in d_r.items():
            if k not in d_m:
                return False
            elif d_m[k] < v:
                return False
        return True