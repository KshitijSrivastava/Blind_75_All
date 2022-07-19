


"""
1 2 3 
4 5 6 
7 8 9

-> 

3 2 1
6 5 4
9 8 7

->

7 4 1
8 5 2
9 6 3

(0,0)   (0,1)   (0,2)
(1,0)   (1,1)   (1,2)
(2,0)   (2,1)   (2,2)

-----------------------------------------------------

0,0 0,1 0,2 0,3
1,0 1,1 1,2 1,3
2,0 2,1 2,2 2,3
3,0 3,1 3,2 3,3



"""

# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            
            start = 0
            end = n - 1
            
            while start < end:
                matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                start += 1
                end -= 1
                
        for i in range(n):
            for j in range(n):
                
                if i + j >= n:
                    continue
                
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
                
        return matrix