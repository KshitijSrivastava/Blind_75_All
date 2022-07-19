

#few test cases didn't pass

class Solution:
    def myAtoi(self, s: str) -> int:
        
        n = len(s)
        minus = None
        
        result = 0
        i = 0
        
        while i < n:
            
            if s[i] == " ":
                pass
            
            elif s[i] == "-" and minus == None:
                minus = True
            
            elif s[i] == "+" and minus == None:
                minus =  False
                
            elif s[i] in string.ascii_letters or s[i] in ["+", "-", "."]:
                break
                
            elif s[i].isnumeric():
                result = (result * 10) + int(s[i])
            
            i += 1
            
        if minus:
            result = result * -1
            
        if result > pow(2,31) - 1:
            result = pow(2,31) - 1
        
        elif result < (-1 * pow(2,31) ):
            result = -1 * pow(2,31)
            
            
        return result
            
        