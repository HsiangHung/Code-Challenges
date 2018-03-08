## [Leetcode#121] Best Time to Buy and Sell Stock
##
##  maximum profit is given by, minimum price bought, and maximum price sold
##  but maximum price needs to be behind minimum price
##
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            
        return max_profit