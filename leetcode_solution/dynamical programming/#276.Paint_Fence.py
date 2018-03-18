# [#276] Paint Fence
#
#  at the post which is going to pain, its color should be neither same as 
#  previous one nor the previous previous one. so (k-1)*dp[x-1] and (k-1)*dp[x-2]
#
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k ==0: return 0
        
        dp = {1: k, 2: k**2}
        
        num_posts = 3
        while num_posts <= n:
            dp[num_posts] = (k-1)*dp[num_posts-1] + (k-1)*dp[num_posts-2]
            num_posts += 1
            
        return max(dp[n], 0)