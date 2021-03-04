#  256. Paint House (medium)
#  https://leetcode.com/problems/paint-house/
#
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0: return 0
        
        dp = costs[0]
        
        for i in range(1, len(costs)):
            dp_0 = min(dp[1], dp[2]) + costs[i][0]
            dp_1 = min(dp[0], dp[2]) + costs[i][1]
            dp_2 = min(dp[0], dp[1]) + costs[i][2]
            dp = [dp_0, dp_1, dp_2]
            
        return min(dp)