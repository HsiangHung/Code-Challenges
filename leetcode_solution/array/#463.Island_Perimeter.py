#  463. Island Perimeter (easy)
#  https://leetcode.com/problems/island-perimeter/
# 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        Just simply count perimeter as long as grid[x] != grid[neighbor]
        consider if boundary, add one more perimeter count 
        '''
        perimeter = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                
                if grid[y][x] == 1:
                    
                    if y == 0: perimeter += 1
                    if x == 0: perimeter += 1
                        
                    if y == len(grid)-1: perimeter += 1
                    if x == len(grid[0])-1: perimeter += 1
                        
                    if y > 0 and grid[y-1][x] == 0:
                        perimeter += 1
                        
                    if x > 0 and grid[y][x-1] == 0:
                        perimeter += 1
                        
                else:
                    
                    if y > 0 and grid[y-1][x] == 1:
                        perimeter += 1
                        
                    if x > 0 and grid[y][x-1] == 1:
                        perimeter += 1
                
                # print (y,x, perimeter)
                        
        return perimeter
                        
                    
                    
                        
                