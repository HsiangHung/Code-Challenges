#  122. Best Time to Buy and Sell Stock II (easy)
#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#
class Solution:
    '''
    https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii/note/177787
    '''
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0 
        for i in range(1, len(prices)):
            profit += max(0, prices[i]-prices[i-1])
            
        return profit

#
#
# solution-2: check every possible trade combination. This sol passed 199/200 test cases,
# but time exceeds.
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        if len(prices) <= 1: return 0
        
        dp = {-1: 0, 0: 0, 1: max(0, prices[1]-prices[0])}
        for i in range(2, len(prices)):
            profit = dp[i-1]
            j = i-1
            while j >= 0:
                profit = max(max(0, prices[i]-prices[j]) + dp[j-1], profit)
                j -= 1

            dp[i] = profit

        return dp[len(prices)-1]