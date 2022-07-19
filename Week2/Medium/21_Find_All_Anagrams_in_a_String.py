
# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution:
    def create_string_dict(self, word):
        d = {}
        for char in word:
            if char not in d:
                d[char] = 0
            d[char] += 1
        return d
    
    def insert_char_dict(self, char, d):
        if char not in d:
            d[char] = 0
        d[char] += 1
        return d
    
    def delete_char_dict(self, char, d):
        if char not in d:
            return d
        if d[char] == 1:
            del d[char]
            return d
        d[char] -= 1
        return d

    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        small = p
        big = s
        
        output = []
        
        n_s = len(small)
        n_b = len(big)
        
        if n_b < n_s:
            return output
        
        d_small = self.create_string_dict(small)
        d_win = {}
        
        i = 0
        j = 0
        
        while j < n_s:
            d_win = self.insert_char_dict(big[j], d_win)
            j += 1
            
        if d_win == d_small:
            output.append(0)
            
            
        while j < n_b:
            d_win = self.delete_char_dict(big[i], d_win)
            d_win = self.insert_char_dict(big[j], d_win)
            
            i += 1
            j += 1
            
            if d_win == d_small:
                output.append(i)
                
        return output