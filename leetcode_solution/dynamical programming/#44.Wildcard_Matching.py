#  44. Wildcard Matching (hard)
#  https://leetcode.com/problems/wildcard-matching/
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Inspired by 10. Regular Expression Matching, here we have similar manner to solve.
        #10 tutorial: https://www.youtube.com/watch?v=l3hda49XcDE
        
        * the only difference is "*" can be any sequence. 
        
        *Dynamical programming rules:
        dp[i][j] =
           a. if s[i] == p[j] or p[j] == "?", dp[i][j] = dp[i-1][j-1]
           b. if p[j] == "*", dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]
           c. otherwise False
        
        e.g. "a*c?b" match "adceb"? 
        
             start with 
            
               0 1 2 3 4 5                0 1 2 3 4 5
                 a * c ? b                  a * c ? b
          0   T                       0   T F F F F F
          1 a F                  =>   1 a F
          2 d F                       2 d F
          3 c F                       3 c F
          4 e F                       4 e F
          5 b F                       5 b F
           
          after rules:
        
              0 1 2 3 4 5                
                a * c ? b               
          0   T F F F F F                      
          1 a F T T F F F                
          2 d F F T F F F             
          3 c F F T T F F           
          4 e F F T F T F             
          5 b F F T F F T                       
        '''
        dp = []
        for i in range(len(s)+1):
            dp.append([False]*(len(p)+1))
            
        dp[0][0] = True
        
        for i in range(len(p)):
            if p[i] == "*":
                dp[0][i+1] = dp[0][i]
        
        for y in range(len(s)):
            for x in range(len(p)):
                if s[y] == p[x] or p[x] == "?":
                    dp[y+1][x+1] = dp[y][x] 
                elif p[x] == "*":
                    dp[y+1][x+1] = dp[y][x] or dp[y][x+1] or dp[y+1][x]
        
        return dp[-1][-1]
