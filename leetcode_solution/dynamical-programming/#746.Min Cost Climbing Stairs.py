# [#746] Min Cost Climbing Stairs
#
#
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 2:
            return min(cost)
        
        min_cost = {0: cost[0], 1: min(cost[0], cost[1]), 2: min(cost[0]+cost[2], cost[1])}
        
        step = 3
        while step < len(cost):
            min_cost[step] = min(min_cost[step-1]+cost[step], min_cost[step-2]+cost[step-1])
            step += 1
            

        return min_cost[len(cost)-1]