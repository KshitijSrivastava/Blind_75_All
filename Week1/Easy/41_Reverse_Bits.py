

"""

000110
left_mask = 2   (000010)
right_mask = 16 (010000)


Ans
011000
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        
        left_mask = pow(2,31)
        right_mask = 1
        
        
        while left_mask > right_mask:
            
            left_value = left_mask & n
            right_value = right_mask & n
            
            #print(left_value, right_value)
            
            if left_value == 0 and right_value == 0:
                pass
            elif left_value != 0 and right_value != 0:
                pass
            else:
                n = n ^ left_mask
                n = n ^ right_mask
            
            left_mask = left_mask >> 1
            right_mask = right_mask << 1
        return n