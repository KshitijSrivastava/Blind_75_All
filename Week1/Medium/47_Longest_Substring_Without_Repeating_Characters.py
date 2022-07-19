

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def add_to_dict(self, d, char):
        if char not in d:
            d[char] = 0
        d[char] += 1
        
        return d

    def delete_from_dict(self, d, char):
        if char not in d:
            raise Exception()
        elif d[char] == 1:
            del d[char]
        else:
            d[char] -= 1
            
        return d
        
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        max_length = 0
        
        win = {}
        win_ele = 0
        
        i = 0
        j = 0
        
        while j < n:
            
            #add elements
            if len(win) == win_ele:
                
                if win_ele > max_length:
                    max_length = win_ele
                    
                win = self.add_to_dict(win, s[j])
                win_ele += 1
                j += 1
                
            else:
                
                win = self.delete_from_dict(win, s[i])
                win_ele -= 1
                i += 1
        
        if len(win) == win_ele and win_ele > max_length:
            max_length = win_ele
            
        return max_length