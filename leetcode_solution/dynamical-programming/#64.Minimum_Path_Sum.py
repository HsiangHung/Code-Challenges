#  64. Minimum Path Sum (medium)
#  https://leetcode.com/problems/minimum-path-sum/
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = []
        for _ in range(len(grid)):
            dp.append([0]*len(grid[0]))
            
        dp[0][0] = grid[0][0]
        for x in range(1, len(grid[0])):
            dp[0][x] = dp[0][x-1] + grid[0][x]
        
        for y in range(1, len(grid)):
            dp[y][0] = dp[y-1][0] + grid[y][0]
                
        for y in range(1, len(grid)):
            for x in range(1, len(grid[0])):
                dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + grid[y][x]
                
        return dp[len(grid)-1][len(grid[0])-1]
                
    
# NOTE using min heap or BFS still time exceeds.
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         heap = [(grid[0][0], 0, 0)]
#         while heap:
#             pathSum, x, y = heapq.heappop(heap)
#             if x == len(grid[0])-1 and y == len(grid)-1:
#                 return pathSum
#             if x < len(grid[0])-1:
#                 heapq.heappush(heap, (pathSum + grid[y][x+1], x+1, y))
#             if y < len(grid)-1:
#                 heapq.heappush(heap, (pathSum + grid[y+1][x], x, y+1))
#         return pathSum
         
                  