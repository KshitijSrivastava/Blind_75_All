
# https://leetcode.com/problems/flood-fill/

class Solution:
    def insideGrid(self, i, j, nrows, ncols):
        return i >= 0 and i < nrows and j >= 0 and j < ncols
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        nrows = len(image)
        ncols = len(image[0])
        
        visited = set()
        
        prev_color = image[sr][sc]
        
        def DFS(visited, i, j):
            nonlocal nrows, ncols, prev_color
            
            image[i][j] = color
            
            for di, dj in [ (0,1), (1,0), (-1, 0), (0,-1)]:
                new_i = i + di
                new_j = j + dj
                
                if self.insideGrid(new_i, new_j, nrows, ncols) and image[new_i][new_j] == prev_color and (new_i, new_j) not in visited:
                    visited.add( (new_i, new_j) )
                    DFS(visited, new_i, new_j)
        
        DFS(visited, sr, sc)
        return image
            