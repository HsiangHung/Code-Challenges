#  200. Number of Islands
#  https://leetcode.com/problems/number-of-islands/
# 
class Solution(object):
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    self.DFS(x, y, grid)
                    n_islands += 1
        return n_islands
    
    def DFS(self, x, y, grid):
        if grid[y][x] == "0": return
        
        grid[y][x] = "0"
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + dx < len(grid[0]) and  0 <= y + dy < len(grid):
                self.DFS(x+dx, y+dy, grid)
   