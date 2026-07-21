#
#   931. Minimum Falling Path Sum
#   
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        failling path only x = [x-1, x, x+1], we can use dp[row][x]
        for dp[row][x+dx] = min(dp[row-1][x] + matrix[row][x+dx], dp[row][x+dx])
        where dx = [-1,0,1]
        """

        n = len(matrix)

        dp = []
        for _ in range(n):
            dp.append([float("inf")]*n)
        
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for row in range(1, n):
            for x in range(n):
                for dx in [-1, 0, 1]:
                    if 0 <= x + dx < n:
                        dp[row][x+dx] = min(dp[row-1][x] + matrix[row][x+dx], dp[row][x+dx])

        return min(dp[n-1])
