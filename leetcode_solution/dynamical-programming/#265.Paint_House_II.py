#  265. Paint House II (Hard)
#  https://leetcode.com/problems/paint-house-ii/
#
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        '''
        refer 256 paint house, still dynamical programming:
        https://leetcode.com/problems/paint-house/submissions/
        consider the cost using current color and previous color as matrix.
        time complexity O(nk*k)
        '''
        if len(costs) == 0: return 0
        
        houses, colors = len(costs), len(costs[0])
        
        dp = costs[0]
        for i in range(1, houses):
                        
            update = []
            for j in range(colors):
                min_cost = 2**31-1
                for k in range(colors):
                    if j != k:
                        min_cost = min(min_cost, dp[k])
                update.append(min_cost+costs[i][j])
                        
            dp[:] = update[:]
                        
        return min(dp)