
 # https://leetcode.com/problems/powx-n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return self.myPow( 1/x, n * -1 )
        
        if n % 2 == 0:
            
            value = self.myPow(x, n // 2)    
            return value * value
        else:
            value = self.myPow(x, n // 2 )
            return x * value * value
        