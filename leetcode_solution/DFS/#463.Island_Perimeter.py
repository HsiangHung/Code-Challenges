#  463. Island Perimeter (easy)
#  https://leetcode.com/problems/island-perimeter/
# 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        Just simply count perimeter as long as grid[x] != grid[neighbor]
        consider if boundary, add one more perimeter count 
        '''

        def helper(x: int, y: int, grid: List[List[int]]) -> int:
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or grid[x][y] == 0:
                return 1

            if grid[x][y] == 2:
                # checked, not water. So not contribute perimeter
                return 0
            
            perimeter = 0
            grid[x][y] = 2
            for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                perimeter += helper(x + dx, y + dy, grid)
            return perimeter

        if not grid: 
            return 0

        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += helper(i, j, grid)

        return perimeter