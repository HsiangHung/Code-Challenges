#  518. Coin Change 2 (medium)
#  https://leetcode.com/problems/coin-change-2/
#
class Solution:
    '''
    amount = 10, [1,2,5]
    sorted coins in descending order: [5,2,1]
    
    DFS + memory save dp[(amount, coins[0])]; otherwise time exceeds
    each recursion, move amount = amount - coins[0], and coins = coins[1:]
    '''
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        coins = sorted(coins, reverse=True)
        self.dp = {}
        return self.DFS(amount, coins)        
        
    def DFS(self, amount, coins):
        if amount == 0: return 1
        if amount < 0: return 0
        
        if len(coins) == 0 or coins[-1] > amount: return 0
        
        if (amount, coins[0]) in self.dp: return self.dp[(amount, coins[0])] 
        
        i, comb = (amount // coins[0]), 0 
        while i >= 0:                        
            comb += self.DFS(amount-i*coins[0], coins[1:])
            i -= 1
            
        self.dp[(amount, coins[0])] = comb
        
        return comb