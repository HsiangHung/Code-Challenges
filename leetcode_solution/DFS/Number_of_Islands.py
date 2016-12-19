## [Leetcode#200] Number of Islands
## 
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []: return 0
        
        m = len(grid[0])
        n = len(grid)
        
        num_island = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == u'1':
                    num_island +=1
                    self.DFS(grid, x, y)
                    
        return num_island
                    
                    
    def DFS(self, grid, x, y):
        grid[y][x] =u'0'
        if x+1 < len(grid[0]) and grid[y][x+1] ==u'1':
            self.DFS(grid, x+1, y)
        if x-1 >= 0 and grid[y][x-1] ==u'1':
            self.DFS(grid, x-1, y)
        if y+1 < len(grid) and grid[y+1][x] ==u'1':
            self.DFS(grid, x, y+1)
        if y-1 >= 0 and grid[y-1][x] ==u'1':
            self.DFS(grid, x, y-1)
            

