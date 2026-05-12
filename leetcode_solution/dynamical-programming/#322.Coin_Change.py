#  322. Coin Change (medium)
#  https://leetcode.com/problems/coin-change/
#
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        This cannot use DFS, too many ways. Use dynamical programming.
        
        Start from dp[min(coins)] and has increment of 1, not min(coins)
        Otherwise we will miss answer.
        
        Corner cases: 
        1. coins = [3,7,9], amount = 20. Coins are 3+3+7. If using increment =3, we cannot get it.
        2. coins = [1,2147483647], amount = 2
        '''
        if amount == 0: return 0        
        
        token = min(coins)
        if token > amount: return -1

        dp = {x: 1 for x in coins}
        i = min(coins) + 1
        while i <= amount:
            
            for x in coins:
                if i - x in dp:
                    if i not in dp:
                        dp[i] = dp[i-x] + 1
                    else:
                        dp[i] = min(dp[i], dp[i-x] + 1)
                        
            i += 1  # NOTE, the amount needs to jump increment of 1. 
                    # if coins[3,7,9] and increment = 3, we will miss anwer.
                                    
        return dp[amount] if amount in dp else -1