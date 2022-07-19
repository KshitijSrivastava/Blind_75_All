
# https://leetcode.com/problems/shortest-path-to-get-food/


class Solution:
    def find_start_position(self, grid):
        
        start_i = 0
        start_j = 0
        
        nrows = len(grid)
        ncols = len(grid[0])
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "*":
                    start_i = i
                    start_j = j
                    break
        
        return (start_i, start_j)
    
    def isInsideGrid(self, i, j, nrows, ncols):
        return i >= 0 and i < nrows and j >= 0 and j < ncols
    
    def getFood(self, grid: List[List[str]]) -> int:
        
        nrows = len(grid)
        ncols = len(grid[0])
        
        start_i, start_j = self.find_start_position(grid)
        
        queue = []
        queue.append( (start_i, start_j, 0) )
        
        visited = set()
        visited.add( (start_i, start_j) )
        
        while queue:
            
            i, j, level = queue.pop(0)
            
            
            if grid[i][j] == "#":
                return level
            elif grid[i][j] == "X":
                continue
            
            for di, dj in [ (0,1), (1,0), (-1,0), (0,-1) ]:
                new_i = i + di
                new_j = j + dj
                
                if (new_i, new_j) not in visited and self.isInsideGrid(new_i, new_j, nrows, ncols):
                    visited.add( (new_i, new_j) )
                    queue.append( (new_i, new_j, level + 1) )
        return -1