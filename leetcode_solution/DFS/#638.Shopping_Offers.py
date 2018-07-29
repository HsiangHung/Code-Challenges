## [# 638] Shopping Offers
#
#
#
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        min_cost = self.cost(price, needs)
        for deal in special:
                    
            if self.isDealWork(deal, needs):
                remain = needs[:]
                for i in range(len(needs)):
                    remain[i] -= deal[i]
                min_cost = min(min_cost, deal[-1] + self.shoppingOffers(price, special, remain))
            else:
                min_cost = min(min_cost, self.cost(price, needs))
                
        return min_cost
            
                
    def isDealWork(self, deal, needs):
        '''check if any number of items in deal > needs'''
        isDealWork = True
        for i in range(len(needs)):
            if deal[i] > needs[i]:
                isDealWork = False
        return isDealWork
    
    def cost(self, price, needs):
        '''given a needs, compute cost'''
        cost = 0
        for i in range(len(needs)):
            if needs[i] != 0:
                cost += needs[i] * price[i]
        return cost