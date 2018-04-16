# [#276] Paint Fence
#
#  at the post which is going to pain, its color should be neither same as 
#  previous one nor the previous previous one. so (k-1)*dp[x-1] and (k-1)*dp[x-2]
#
 if k == 0 or n ==0:
            return 0
        
        ##  e.g. k = 3, 
        ##  n = 3 we have 24 ways:
        ##  
        ##     , 112, 113, 121, 122, 123, 131, 132, 133
        ##  211, 212, 213, 221,    , 223, 231, 232, 233
        ##  311, 312, 313, 321, 322, 323, 331, 332,
        ##   
        ##  for n =4, we have to be careful of [211,311,122,322,133,233] not become [2111,1222,2333...]
        ##
        ##  (1) it's safe to add digits which are different from the last digit, there are dp[i-1] * (k-1) choices
        ##  [211, 112, 312, 232..] => [211+2, 211+3, 112+1, 112+3, 312+1, 312+3, 232+1, 232+3,...]
        ##
        ##  (2) then we consider if the last digit is the same as the first digit, but different from second 
        ##  last digit, there are dp[i-2] * (k-1) choices
        ##  [11, 12, 13, 21, 31,..] => [11+22, 11+33, 12+11, 12+33, 13+11, 13+22, 21+22, 21+33, 31+22, 31+33...] 
        ##
        dp = {1: k, 2: k**2}
        post = 3
        while post <= n:
            dp[post] = (k-1)*dp[post-1]+(k-1)*dp[post-2]
            post += 1
            
        return dp[n]