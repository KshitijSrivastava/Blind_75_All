
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        firstRow = False
        firstCol = False
        #storing the state of first row
        for j in range(num_cols):
            if matrix[0][j] == 0:
                firstRow = True
                
        #storing the state of first column
        for i in range(num_rows):
            if matrix[i][0] == 0:
                firstCol = True
        
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = -1
                    matrix[0][j] = -1
        
        #Make rows zero
        for i in range(1, num_rows):
            if matrix[i][0] == -1:
                for j in range(num_cols):
                    matrix[i][j] = 0
                    
        #Make column zero
        for j in range(1, num_cols):
            if matrix[0][j] == -1:
                for i in range(num_rows):
                    matrix[i][j] = 0
                    
        if firstRow:
            for j in range(num_cols):
                matrix[0][j] = 0
                
        if firstCol:
            for i in range(num_rows):
                matrix[i][0] = 0
                
        return matrix