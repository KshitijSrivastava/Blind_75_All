
# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def get_arr(self, string):
        stack = []
        for char in string:
            if char != "#":
                stack.append(char)
            elif len(stack) != 0 and char == "#":
                stack.pop()
                
        return stack
        
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_s = self.get_arr(s)
        s_t = self.get_arr(t)
        
        return s_s == s_t