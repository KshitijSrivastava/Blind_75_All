
 #https://leetcode.com/problems/valid-sudoku/

 class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = { i: [] for i in range(1, 9+1) }
        col = { i: [] for i in range(1, 9+1) }
        
        sub_box = { (i, j): [] for i in range(3) for j in range(3) }
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    continue
                
                if i in row[ int(board[i][j]) ]:
                    return False
                
                row[ int(board[i][j]) ].append(i)
                
                if j in col[ int(board[i][j]) ]:
                    return False
                
                col[ int(board[i][j]) ].append(j)
                
                if int(board[i][j]) in sub_box[(i//3, j//3) ]:
                    return False
                
                sub_box[ (i // 3, j // 3) ].append( int(board[i][j]) )
                
        return True