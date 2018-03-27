# [#62] Unique Paths
#
#
#
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #return self.recursion_count(m, n)
        dp = [[1]*m]+[[0]*m]*(n-1)
        for i in range(n):
            dp[i][0] = 1
         
        for y in range(1, n):
            for x in range(1, m):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
            
        return dp[n-1][m-1]
        
        
        
    def recursion_count(self, m, n):
        '''
        This method will exceed time limit by Leetcode, but works
        '''
        if m == 1 and n == 1: return 1
        num_paths = 0
        if m > 1:
            num_paths += self.uniquePaths(m-1, n)            
        if n > 1:
            num_paths += self.uniquePaths(m, n-1)
        return num_paths