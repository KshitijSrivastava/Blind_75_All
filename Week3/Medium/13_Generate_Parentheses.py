
# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def isValid(self, arr):
        stack = []
        
        for char in arr:
            
            if len(stack) == 0 or char == "(":
                stack.append(char)
            elif len(stack) == 0 and char == ")":
                return False
            elif stack[-1] == "(" and char == ")":
                stack.pop()
            else:
                return False
                
        return len(stack) == 0
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        
        def recur(idx, n, curr):
            if idx == 2 * n:
                
                if self.isValid(curr):
                    output.append( "".join(curr[::]) )
                return
            
            curr.append( "(" )
            recur(idx + 1, n, curr)
            curr.pop()
            
            curr.append(")")
            recur(idx + 1, n, curr)
            curr.pop()
            
        recur(0, n, [])
        return output
            