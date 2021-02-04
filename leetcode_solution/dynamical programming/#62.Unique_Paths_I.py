#  62. Unique Paths (medium)
#  https://leetcode.com/problems/unique-paths/
#
#
class Solution(object):
    '''
    using DM. initialize first row/column all = 1, since only one way to get the x=0 or y=0 boundary

    dp[y][x] = dp[y-1][x] + dp[y][x]

    e.g. m=2, n= 3                    m=n=3
    r\c 0  1  2                  r\c  0  1  2           
     0  1  0  0  =>  1  1  1      0   1  1  1  =>    1  1  1
     1  1  0  0      1  2  3      1   1  0  0        1  2  3 
                                  2   1  0  0        1  3  6
    '''
    def uniquePaths(self, m, n):
        if m == 1 and n == 1: return 1
        
        dp = []
        for _ in range(m):
            dp.append([0]*n)
            
        for x in range(n):
            dp[0][x] = 1
            
        for y in range(m):
            dp[y][0] = 1
            
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
                
        
        return dp[m-1][n-1]