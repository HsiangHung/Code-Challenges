## [Leetcode#695] Max Area of Island
##
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    max_area = max(max_area, self.get_area(grid, x, y))
                
        return max_area
    
    
    def get_area(self, grid, x, y):
        if grid[y][x] == 0: return 0
        
        grid[y][x] = 0  ## after checking, need to turn to 0; otherwise unlimted recursion
        
        area = 1
        if x-1 >= 0:
            area += self.get_area(grid, x-1, y)
            
        if y-1 >= 0:
            area += self.get_area(grid, x, y-1)
            
        if x+1 < len(grid[0]):
            area += self.get_area(grid, x+1, y)
            
        if y+1 < len(grid):
            area += self.get_area(grid, x, y+1)
        
        return area