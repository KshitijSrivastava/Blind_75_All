
 # https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        output = []
        
        total = 0
        i = 0
        
        n_a = len(a)
        n_b = len(b)
        
        i_a = n_a - 1
        i_b = n_b - 1
        
        carry = 0
        while i_a >= 0 and i_b >= 0:
            
            val_a = int( a[i_a] )
            val_b = int( b[i_b] )
            
            total = val_a + val_b + carry
            
            char = str(total % 2)
            carry = total // 2
            
            output.append( char )
            
            i_a -= 1
            i_b -= 1
            
        while i_a >= 0:
            val_a = int( a[i_a] )
            total = val_a + carry
            
            char = str(total % 2)
            carry = total // 2
            
            output.append( char )
            i_a -= 1
            
        while i_b >= 0:
            val_b = int( b[i_b] )
            
            total =  val_b + carry
            
            char = str(total % 2)
            carry = total // 2
            
            output.append( char )
            i_b -= 1
            
        if carry != 0:
             output.append( "1" )
                
        return "".join(output[::-1])
            