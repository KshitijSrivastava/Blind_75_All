

"""
# https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

class Solution:
    def insideGrid(self, i, j, nrows, ncols):
        return i >= 0 and i < nrows and j >= 0 and j < ncols
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        nrows = len(heights)
        ncols = len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        
        def DFS(i,j, ocean_set, prevHeight):
            nonlocal nrows, ncols
            #print(i,j)
            if (i,j) in ocean_set or not self.insideGrid(i,j, nrows, ncols) or prevHeight > heights[i][j]:
                return
            ocean_set.add( (i,j) )
            
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                new_i = i + di
                new_j = j + dj
                
                DFS(new_i, new_j, ocean_set, heights[i][j])
        
        
        #top row (pacific) and the bottom row (atlantic)
        for j in range(ncols):
            DFS(0, j, pacific, heights[0][j] )
            DFS(nrows - 1, j, atlantic, heights[nrows - 1][j])
            
        #left column (pacific) and right column (atlantic)
        for i in range(nrows):
            DFS(i, 0, pacific, heights[ i ][ 0 ] )
            DFS(i, ncols - 1, atlantic, heights[i][ ncols - 1 ])
            
        output = []
        for i in range(nrows):
            for j in range(ncols):
                if (i,j) in pacific and (i,j) in  atlantic:
                    output.append( [i,j] )
        return output