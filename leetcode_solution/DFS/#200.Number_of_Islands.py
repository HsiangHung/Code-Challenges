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
                    num_island += 1
                    self.DFS(m, n, x, y, grid)
                    
        return num_island
    
    def DFS(self, m, n, x, y, grid):
        if grid[y][x] == u'0': return
        
        grid[y][x] = u'0'
        
        if x > 0:
            self.DFS(m, n, x-1, y, grid)
        
        if x < m-1:
            self.DFS(m, n, x+1, y, grid)
            
        if y > 0:
            self.DFS(m, n, x, y-1, grid)
        
        if y < n-1:
            self.DFS(m, n, x, y+1, grid)
            

