
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {}
        d[2] = "abc"
        d[3] = "def"
        d[4] = "ghi"
        d[5] = "jkl"
        d[6] = "mno"
        d[7] = "pqrs"
        d[8] = "tuv"
        d[9] = "wxyz"
        
        output =[]
        
        def recur(idx, n, curr):
            nonlocal output, d
            if idx == n:
                output.append( "".join(curr[::]) )
                return
                
            for char in d[ int( digits[idx] ) ]:
                curr.append( char )
                recur(idx + 1, n, curr)
                curr.pop()
        idx = 0
        n = len(digits)
        
        if n == 0:
            return []
        
        recur(idx, n, [])
        
        return output