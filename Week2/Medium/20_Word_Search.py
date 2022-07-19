


class Solution:
    def word_search(self, board, m, n, i, j, word, index ):
        print(i, j, index)
        if index == len(word):
            print("Found")
            return "Found"
        
        char = board[i][j]
        board[i][j] = "$"
        
        top =  bottom = left = right = False
        
        #top
        if i - 1 >= 0 and board[i-1][j] == word[index]:
            top = self.word_search( board, m, n, i-1, j, word, index+1 )
        
        #bottom
        if i + 1 < m and board[i+1][j] == word[index]:
            bottom = self.word_search( board, m, n, i+1, j, word, index+1 )
        #left
        if j - 1 >= 0 and board[i][j-1] == word[index]:
            left = self.word_search( board, m, n, i, j-1, word, index+1 )
        #right
        if j + 1 < n and board[i][j+1] == word[index]:
            right = self.word_search( board, m, n, i, j+1, word, index+1 )
            
        board[i][j] = char
        
        return top or bottom or left or right
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len( board[0]) 
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    char = board[i][j]
                    board[i][j] = "$"
                    returned_val =  self.word_search(board, m, n, i, j, word, 1)
                    board[i][j] = char
                    print(returned_val)
                    if returned_val:
                        return True  
        return False