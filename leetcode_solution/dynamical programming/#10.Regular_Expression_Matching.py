#  10. Regular Expression Matching (hard)
#  https://leetcode.com/problems/regular-expression-matching/
#
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        tutorial: https://www.youtube.com/watch?v=l3hda49XcDE
        
        dynamical programming rules 
        dp[i][j] =
           a. if s[i] == p[j] or p[j] == ".", dp[i][j] = dp[i-1][j-1]
           b. if p[j] == "*", dp[i][j] = (dp[i][j-2]) | (dp[i-1][j] if s[i] == p[j-1])
           c. otherwise False
        
        e.g. "xa*b.c" mathc "xaabyc"? 
        
            start with 
            
               0 1 2 3 4 5 6 
                 x a * b . c      
          0   T      
          1 x F          
          2 a F 
          3 a F         
          4 b F 
          5 y F 
          6 c F 
        
           NOTE the first row needs to be run, not default as [T F F F ...]
                e.g. s = "aab", p = "c*a*b", then dp[0][2] = True 
        
              0 1 2 3 4 5 6 (j)
         (i)    x a * b . c      i.e. i=2, j=2, s[2]=p[2]="a", dp[2][2] = dp[1][1] = T
          0   T F F F F F F     
          1 x F T F T F F F           i=3, j=3, s[3]="a", p[3]="*", dp[3][1] | (dp[2][3] if s[3]==p[2]) = T
          2 a F F T T F F F
          3 a F F F T F F F           i=4, j=1, s[4]="b", p[1]="x", dp[4][1] = F
          4 b F F F F T F F
          5 y F F F F F T F
          6 c F F F F F F T
        '''
        
        dp = []
        for i in range(len(s)+1):
            dp.append([False]*(len(p)+1))
            
        dp[0][0] = True
        
        # note the first row needs to be run, not default as [T F F F ...]
        for j in range(1, len(p)+1):
            if p[j-1] == "*": dp[0][j] = dp[0][j-2]
        
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if s[i-1] == p[(j-1)-1] or p[(j-1)-1] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        return dp[len(s)][len(p)]
 