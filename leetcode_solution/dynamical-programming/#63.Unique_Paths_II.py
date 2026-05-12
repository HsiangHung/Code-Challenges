#  63. Unique Paths II (medium)
#  https://leetcode.com/problems/unique-paths-ii/
#
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        If implementing DFS or BFS to solve this problem, always time exceeds.
        Only use dynamical programming can overcome the issue.
        '''
        if obstacleGrid[0][0] == 1: return 0
        
        dp = []
        for i in range(len(obstacleGrid)):
            dp.append([0]*len(obstacleGrid[0]))
                
        dp[0][0] = 1
            
        for y in range(len(obstacleGrid)):
            for x in range(len(obstacleGrid[0])):
                
                if x == 0 and y == 0: continue
                
                if obstacleGrid[y][x] == 0:
                    if x > 0 and y > 0:
                        dp[y][x] = dp[y][x-1] + dp[y-1][x]
                    elif x > 0:
                        dp[y][x] = dp[y][x-1]
                    elif y > 0:
                        dp[y][x] = dp[y-1][x]

        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        DFS or BFS works, but time exceeds.
        '''
        if obstacleGrid[0][0] == 1: return 0
        
        self.num_paths = 0
        self.DFS(0, 0, obstacleGrid)
        return self.num_paths 
        
        
    def DFS(self, x, y, grid):
                
        if x == len(grid[0])-1 and y == len(grid)-1: 
            self.num_paths += 1
            return
                    
        if x+1 <= len(grid[0])-1 and grid[y][x+1] == 0:
            self.DFS(x+1, y, grid)
                
        if y+1 <= len(grid)-1 and grid[y+1][x] == 0:
            self.DFS(x, y+1, grid)