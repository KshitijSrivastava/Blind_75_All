
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)                                 #Numbers of rows
        n = len(matrix[0])                              #number of columns
        
        i = 0                                           #points to top right corner
        j = n-1
        
        while i >= 0 and i < m and j >= 0 and j < n:    #whilwe location inside the matrix
            if matrix[i][j] == target:                  #if matix value ta the location equals tar
                return True
            elif matrix[i][j] < target:                 
                i += 1
            else:
                j -= 1
                
        return False
        
        