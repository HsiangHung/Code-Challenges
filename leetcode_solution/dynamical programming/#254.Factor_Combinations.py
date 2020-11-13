# # 254. Factor Combinations
#
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        '''
        This one used dynamical programming + recursion (DFS).
        Need to 
        e.g. 24 = [[2,12]] -> + [[2,2,6]] -> + [[2,2,2,3]] 
                = [[3,8]] -> + [[3,2,4]] -> + [[3,2,2,2]]
                = [[4,6]] -> + [[4,2,3]] 
                
        use dp to save factorization been discovered before
        '''     
        self.dp = {}
        self.DFS(n)
        return self.dp[n] if len(self.dp[n]) > 0 else []
    
        
    def DFS(self, n):
        import numpy as np
        
        if n in self.dp: return # make sure if met before, return to save time
        
        self.dp[n] = []    
        
        if n <= 3: return 
    
        for r in range(2, int(np.sqrt(n))+1):
            if n % r == 0:
                q = n // r
                self.dp[n].append([r, q])
                self.DFS(q)
                for y in self.dp[q]:
                    sol = sorted([r]+y)
                    if sol not in self.dp[n]:  # make sure no duplicated factorization
                        self.dp[n].append(sorted([r]+y))
                     
      
                    
                