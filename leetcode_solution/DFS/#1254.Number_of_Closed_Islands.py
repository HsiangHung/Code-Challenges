#  1254. Number of Closed Islands (medium)
#  https://leetcode.com/problems/number-of-closed-islands/
#
class Solution:
    '''
    idenfity an island, as long as it is not next to board, it is a closed island
    
    NOTE. if the recurion returns something and grid not return, then grid will be not updated.
    
    e.g. original code was 
    
         .....
         grid[y][x] = 1
         isClosed = True
         
         if x > 0 and grid[y][x-1] == 0: 
            isClosed = isClosed and self.DFS(x-1, y, grid)
        
         return isClosed
         
         This won't update grid since not return grid unless return grid too.
    '''
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        num_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    self.isClosed = True
                    self.DFS(x, y, grid)
                    if self.isClosed: num_islands += 1
        return num_islands
    
    def DFS(self, x, y, grid):
           
        grid[y][x] = 1
        
        if x == 0 or x == len(grid[0])-1 or y == 0 or y == len(grid)-1:
            self.isClosed = False
            
        if x > 0 and grid[y][x-1] == 0: 
            self.DFS(x-1, y, grid)
            
        if y > 0 and grid[y-1][x] == 0: 
            self.DFS(x, y-1, grid)
            
        if x < len(grid[0])-1 and grid[y][x+1] == 0:
            self.DFS(x+1, y, grid)
            
        if y < len(grid)-1 and grid[y+1][x] == 0: 
            self.DFS(x, y+1, grid)
