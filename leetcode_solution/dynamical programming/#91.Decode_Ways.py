#  91. Decode Ways (medium)
#  https://leetcode.com/problems/decode-ways/
# 
#
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        This problem is unable to use DFS, for testing case like 
        s = "111111111111111111111111111111111111111111111", time exceeds.          
        We need to use dynamical programming. Return the last dp.
        e.g. s = "2225":
             dp[0] = dp[1] = 1 
             "22":   dp[2] = (dp[1] + "2") & (dp[0] + "22") = 1 + 1 = 2
             "222":  dp[3] = (dp[2] + "2") & (dp[1] + "22") = 2 + 1 = 3
             "2225": dp[4] = (dp[3] + "5") & (dp[2] + "25") = 3 + 2 = 5
             
        e.g. s = "2265":
             dp[0] = dp[1] = 1 
             "22":   dp[2] = (dp[1] + "2") & (dp[0] + "22") = 1 + 1 = 2
             "226":  dp[3] = (dp[2] + "6") & (dp[1] + "26") = 2 + 1 = 3
             "2265": dp[4] = (dp[3] + "5") & (dp[2] + "65") = 3 + 0 = 3

        e.g. s = "2205":
             dp[0] = dp[1] = 1 
             "22":   dp[2] = (dp[1] + "2") & (dp[0] + "22") = 1 + 1 = 2
             "220":  dp[3] = (dp[2] + "0") & (dp[1] + "20") = 0 + 1 = 1
             "2205": dp[4] = (dp[3] + "5") & (dp[2] + "05") = 1 + 0 = 1
             
        e.g. s= "0225"; return 0 since no "0" and no "02"
        '''
        if s[0] == "0": return 0
        
        dp = {0: 1, 1: 1}
        i = 2
        while i <= len(s):
            dp[i] = 0
            if  s[i-2: i] <= "26" and s[i-2] != "0": dp[i] = dp[i-2]
            if s[i-1] != "0": dp[i] += dp[i-1]
            i += 1
        
        return dp[len(s)]
        
