#  254. Factor Combinations (medium)
#  https://leetcode.com/problems/factor-combinations/
#
class Solution:
    def __init__(self):
        self.factors = {} ## save factors for each number, speed up
        
    def getFactors(self, n: int) -> List[List[int]]:
        if n < 3: return []

        ans = []
        i = 2
        while i*i <= n:
            
            if n % i == 0:
                q = n // i
                ans.append([i, q])
                if q not in self.factors:
                    f = self.getFactors(q)
                else:
                    f = self.factors[q]
                for x in f:
                    if x[0] >= i:  # if [3,4] = [3,2,2] and [2,6] = [2,2,3], but make sure no dup
                        ans.append([i]+x)
                
            i += 1
            
        return ans