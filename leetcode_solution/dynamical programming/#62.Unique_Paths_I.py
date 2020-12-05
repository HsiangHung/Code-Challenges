#  62. Unique Paths (medium)
#  https://leetcode.com/problems/unique-paths/
#
#
class Solution(object):
    def uniquePaths(self, m, n):
        if m == 1 and n == 1: return 1
        
        dp = []
        for i in range(m):
            dp.append([0]*n)
            
        dp[0][0] = 1
        for y in range(m):
            for x in range(n):
                
                if x > 0 and y > 0:
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
                elif x > 0:
                    dp[y][x] = dp[y][x-1]
                elif y > 0:
                    dp[y][x] = dp[y-1][x]
                
        return dp[m-1][n-1]