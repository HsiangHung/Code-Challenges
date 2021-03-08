#  638. Shopping Offers (medium)
#  https://leetcode.com/problems/shopping-offers/
#
class Solution:
    '''
    DFS as checking all deal combination.
    e.g. price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
       A  B  have   still need  cost
       0  0  [0,0]  [3,2]       3*$2+2*$5 = $16
       0  1  [1,2]  [2,0]       $10 + 2*$2 = $14
       0  2  [2,4]  
       1  0  [3,0]  [0,2]       $5 + 2*$5 = $15
       1  1  [4,2]
       2  0. [6,0]
       
     so minimum is $14.
    '''
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        min_cost = sum([price[i]*needs[i] for i in range(len(price))])
        if min_cost == 0: return 0
        
        self.min_cost = min_cost
        
        self.DFS(0, special, price, needs)
        return self.min_cost
        
    def DFS(self, cost, special, price, needs):
                
        if len(set(needs)) == 1 and needs[0] == 0:  ## if all needs =0, compare cost
            self.min_cost = min(self.min_cost, cost)
            return
        
        if len(special) == 0: ## if no more deals to search, check items needs to fill and compare cost
            for j in range(len(needs)):  
                if needs[j] > 0:
                    cost += price[j]*needs[j]
            self.min_cost = min(self.min_cost, cost)
            return
        
        i, search = 0, True 
        while search:            
            if i == 0:
                self.DFS(cost, special[1:], price, needs)
                needs2 = needs[:]           ## need to store incoming needs since later it will be changed
            else:
                for j in range(len(needs)):
                    needs[j] -= special[0][j]
                    if needs[j] < 0: 
                        needs[:] = needs2[:] ## <= backtrack, needs[:] = needs2[:], not needs= needs[:]
                        return
                                        
                cost += special[0][-1]
                self.DFS(cost, special[1:], price, needs)

            i += 1
      