#[Leetcode#256] Paint House
#
#  LinkedIn
#
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0: return 0
        if len(costs) == 1: return min(costs[0])
        
        dp = {1: costs[0]}
        house = 2
        while house <= len(costs):
            dp[house] = [costs[house-1][0]+min(dp[house-1][1], dp[house-1][2]),
                         costs[house-1][1]+min(dp[house-1][0], dp[house-1][2]),
                         costs[house-1][2]+min(dp[house-1][0], dp[house-1][1])
                        ]
            house += 1
        
        return min(dp[len(costs)])