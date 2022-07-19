
#https://leetcode.com/problems/rotting-oranges

class Solution:
    def insideGrid(self, i, j, nrows, ncols):
        return i >= 0 and i < nrows and j >= 0 and j < ncols
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrows, ncols = len(grid), len(grid[0])
        
        visited = set()
        queue = []
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 2:
                    queue.append( ( (i,j), 0 ) )
                    visited.add( (i,j) )
                    
        max_time = 0
        while queue:
            #print(queue)
            pos, time = queue.pop(0)
            
            max_time = max(time, max_time)
            
            pos_i, pos_j = pos[0], pos[1]
            
            for di, dj in [ (0,1), (1,0), (-1,0), (0,-1) ]:
                n_i, n_j = pos_i + di, pos_j + dj
                
                if self.insideGrid(n_i, n_j, nrows, ncols) and (n_i, n_j) not in visited and grid[n_i][n_j] == 1:
                    obj = ( (n_i, n_j), time + 1 )
                    queue.append( obj  )
                    visited.add( (n_i, n_j) )
                    
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    return -1
        return max_time
        