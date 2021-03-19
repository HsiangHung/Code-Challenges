#  994. Rotting Oranges (medium)
#  https://leetcode.com/problems/rotting-oranges/
#
class Solution:
    '''
    This is similar to #286. Walls and Gates:
    starting from every rotten orange, and go through all fresh orangs. 
    Every DFS step dist + 1, and if dist < steps, return

    need to consider if no rotten oranges exist (return -1) and no fresh oranges (return 0)
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        steps = []
        for _ in range(len(grid)):
            steps.append([2**31-1]*len(grid[0]))
        
        isRotten, fresh = False, False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    steps[y][x] = -1
                elif grid[y][x] == 2:
                    steps[y][x] = 0
                    isRotten = True
                else:
                    fresh = True

        if not isRotten and not fresh: return 0   # need to consider corner case where no rotten oranges exist
    
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    self.DFS(x, y, grid, steps, 0)
        
        max_step = max(steps[0])
        for y in range(1, len(steps)):
            max_step = max(max_step, max(steps[y]))
        
        return max_step if max_step < 2**31-1 else -1 # if a fresh orange is isolated
        
                    
    def DFS(self, x, y, grid, steps, dist):
        if steps[y][x] == -1: 
            if grid[y][x] == 0: return 
                    
        if dist > steps[y][x]: return
        
        steps[y][x] = dist
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if len(grid[0]) > x+dx >= 0 and len(grid) > y+dy >= 0:
                self.DFS(x+dx, y+dy, grid, steps, dist + 1)
       