## [Leetcode#70] Climbing Stairs
#
#
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n
        
        dp = {1: 1, 2: 2}
        step = 3
        while step <= n:
            dp[step] = dp[step-1] + dp[step-2]
            step += 1
            
        return dp[n]