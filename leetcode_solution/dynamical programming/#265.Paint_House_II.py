# #265. Paint House II (Hard)
#
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        '''
        refer 256 paint house, still dynamical programming:
        https://leetcode.com/problems/paint-house/submissions/
        consider the cost using current color and previous color as matrix.
        time complexity O(nk*k)
        '''
        if costs == []: return 0
        
        dp = {0: costs[0]}
        
        for i in range(1, len(costs)):
            dp[i] = []
            for color in range(len(costs[i])):
                min_cost = min([dp[i-1][prev_color] for prev_color in range(len(costs[i])) if prev_color != color])
                dp[i].append(costs[i][color] + min_cost)
            
        return min(dp[len(costs)-1])
            