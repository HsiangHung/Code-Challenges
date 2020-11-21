#  122. Best Time to Buy and Sell Stock II (easy)
#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#
#  total max profit is given by sum of max local profit
#  when price goes down, we gain max profit by sell previous price to get max local
#  profit.
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        
        sum = 0 
        local_max_profit = 0
        local_min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                sum += local_max_profit
                local_min_price = prices[i]
                local_max_profit = 0
            else:
                local_max_profit = max(local_max_profit, prices[i]-local_min_price)
                
        return sum + local_max_profit