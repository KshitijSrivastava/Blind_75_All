
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def add_char_to_dict(self, d, char):
        if char not in d:
            d[char] = 0
        d[char] += 1
            
        return d
    
    def delete_char_to_dict(self, d, char):
        if char not in d:
            raise Exception()
        elif d[char] == 1:
            del d[char]
        else:
            d[char] -= 1
        return d
    
    
    def characterReplacement(self, s: str, k: int) -> int:
        n_s = len(s)
        
        i = 0
        j = 0
        
        win = {}
        win_ele = 0
        
        max_length = 0
        
        while j < n_s:
            
            if len(win) <= 1 or ( len(win) > 1 and (win_ele - max( win.values() ) ) <= k):
                
                max_length = max(max_length, win_ele)
                
                self.add_char_to_dict(win, s[j])
                win_ele += 1
                j += 1
            
            else:
                
                self.delete_char_to_dict(win, s[i])
                win_ele -= 1
                i += 1
                
            if len(win) <= 1 or ( len(win) > 1 and (win_ele - max(win.values()) ) <= k):
                #print("Yes")
                max_length = max(max_length, win_ele)
            #print(i,j, win_ele, max_length )
                
        return max_length
            