#  1155. Number of Dice Rolls With Target Sum (medium)
#  https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
#
class Solution:
    '''
    https://www.cnblogs.com/Dylan-Java-NYC/p/12196018.html
    
    e.g. 3 f=6 dices, target = 7
    
    d\tar     0  1  2  3  4  5  6  7
    1   dp = [0, 1, 1, 1, 1, 1, 1, 0]
    2   dp = [0, 0, 1, 2, 3, 4, 5, 6]
    3   dp = [0, 0, 0, 1, 3, 6, 10, 15]
    '''
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d*f or target < d: return 0
        
        mod = 1000000007
        
        dp = [0]*(target+1)
        
        dp[0] = 1
        
        i = 1
        while i <= d:
            tmp = [0]*(target+1)
            
            for j in range(1, f+1):
                for k in range(j, target+1):
                    tmp[k] = (tmp[k] + dp[k - j]) % mod
                    
                    
            # print (i, tmp)
            
            dp[:] = tmp[:]
            
            i += 1
        
        return dp[target]
        