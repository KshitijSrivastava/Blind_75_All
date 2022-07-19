
# https://leetcode.com/problems/spiral-matrix/

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        output = []
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        
        left = 0
        right = ncols - 1
        
        top = 0
        bottom = nrows - 1
        
        direction = "r"
        
        i = 0
        j = 0
        
        while left <= right and top <= bottom:
            
            if direction == "r":
                
                while j <= right:
                    output.append( matrix[i][j] )
                    
                    if j == right:
                        break
                    j += 1
                
                i += 1
                top += 1
                direction = "d"
                continue
            
            elif direction == "d":
                while i <= bottom:
                    output.append( matrix[i][j] )
                    
                    if i == bottom:
                        break
                    i += 1
                
                j -= 1
                right -= 1
                direction = "l"
                continue
            
            elif direction == "l":
                while j >= left:
                    output.append( matrix[i][j] )
                    
                    if j == left:
                        break
                    
                    j -= 1
                i -= 1
                bottom -= 1
                direction = "u"
                continue
                
            elif direction == "u":
                
                while i >= top:
                    output.append(matrix[i][j])
                    if i == top:
                        break
                
                    i -= 1
                j += 1
                left += 1
                direction = "r"
        
        return output            