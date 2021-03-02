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
                    max_area = max(max_area, self.get_area(x, y, grid))
                
        return max_area
    
    
    def get_area(self, x, y, grid):
        if grid[y][x] == 0: return 0
        
        grid[y][x] = 0  ## after checking, need to turn to 0; otherwise unlimted recursion
        area = 1
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if len(grid[0]) > x + dx >= 0 and len(grid) > y + dy >= 0 and grid[y+dy][x+dx] == 1:
                area += self.get_area(x+dx, y+dy, grid)
    
        return area