
# https://leetcode.com/problems/number-of-islands/

"""
Space Complexity: O(N * M)
Time COmplexity: O(N * M)
"""

class Solution:
    def insideGrid(self, grid, i, j, nrows, ncols):
        return i >= 0 and i < nrows and j >= 0 and j < ncols
    
    def DFS(self, grid, i, j, nrows, ncols, visited):
        
        for di, dj in [(0,1), (1,0), (-1, 0), (0, -1)]:
            new_i = i + di
            new_j = j + dj
            
            if self.insideGrid(grid, new_i, new_j, nrows, ncols) and grid[new_i][new_j] == '1' and (new_i, new_j) not in visited:
                visited.add( (new_i, new_j) )
                self.DFS(grid, new_i, new_j, nrows, ncols, visited)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        nrows = len(grid)
        ncols = len(grid[0])
        
        visited = set()
        count  = 0
        
        for i in range(nrows):
            for j in range(ncols):
                
                if (i,j) not in visited and grid[i][j] == "1":
                    count += 1
                    visited.add( (i,j) )
                    self.DFS(grid, i, j, nrows, ncols, visited)
                    
        return count
                    
                    