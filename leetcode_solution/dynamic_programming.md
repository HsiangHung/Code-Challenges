
# Dynamic Programming

## Q1: Cut `n` to `1`.
### For an integer number `n >1`, we can have the following operations to update the number until `n=1`: (1) `n-1`  or (2) if `n` can be divided by `2`, then we have `n/2` (3) if `n` can be divided by `3`, then we have `n/3`. Find the minimum number of operations to `n` needed. e.g. 3 times for `n=10`: `10-1=9`, `9/3=3`, `3/3=1`.
```Python
def numWays(n):
    if n == 1: return 0
    dp = {1:0}
    i = 2
    while i <= n:
        dp[i] = dp[i-1]+1 ## n-1 operation
        if i % 2 ==0: dp[i] = min(dp[int(i/2)]+1, dp[i])
        if i % 3 ==0: dp[i] = min(dp[int(i/3)]+1, dp[i])
        i += 1
    return dp[n]
    
print (numWays(10)) ## 15-1-1...: 14 times 15/3 =5, 5-1=4, 4/2 = 2, 2/2 or 2-1 =1 
```

## Q2: Mininum number of coins.
### In a country, there are three type of coins: `{1,7,10}`. Given an amount of $`n`, find the minimum number of coins. e.g. n=16, the minum number of coins is `4` since `{7,7,1,1}`, not `{10,1,1,1,1,1,1}`.
```Python
def numWays(n):
    ## 1, 7, 10
    if n == 1: return 1
    dp = {0:0, 1:1}
    i=2
    while i <= n:
        dp[i] = dp[i-1]+1
        if i >= 7: dp[i] = min(dp[i-7]+1, dp[i])
        if i >= 10: dp[i] = min(dp[i-10]+1, dp[i])
        i += 1
    
    return dp[n]
    
print (numWays(16))
```


### Q3: [Leetcide#139] Word Break
```Python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if s in wordDict: return True
        
        ## doing dynamic programming:
        ## http://bangbingsyb.blogspot.com/2014/11/leetcode-word-break-i-ii.html
        ## e.g. s = 'abcde', dict = {'a','abc', 'b', 'cd', 'e', 'bcd'}
        ##
        ##  check for s[0:i-1], there exists a s[k:i-1] in dict, and also dp[k] = True
        ##     
        ##  (1) start with dp[0] = True
        ##  (2)  dp[1] => s[0:0] => 'a' exist in dict and dp[0] is true, so dp[1] = True
        ##  (3)  dp[2] => s[0:1] => 'ab' doesn't exist in dict 
        ##                          but 'b' yes, and dp[1] = True (meaning has 'a'), so dp[2] = True
        ##  (4)  dp[3] => s[0:2] => 'abc' exits in dict and dp[0] = True, so d[3] = True
        ##                          (even 'bc' not in dict, 'c' not in dict)
        ##  (5)  dp[4] => s[0:3] => 'abcd' not in dict, but 'bcd' in and dp[1] ('a') True, so dp[4] = True
        ##                      or,'cd' in, and dp[2]('a' and 'b') so dp[4] = True
        ##                        (even 'd' not in dict)
        ##  (6)  dp[5] => s[0:4] => 'abcde' not in dict, 'bcde', 'cde', 'de' not in dict
        ##                       but 'e' in dict, and dp[4] ('a'+'bcd') is True, so dp[5] = True
        
        num = len(wordDict)
        
        dp = {0: True}
        
        for i in range(1, len(s)+1):
            if i == 1:
                substr = s[0]
                if substr in wordDict and dp[0] == True: 
                    dp[1] = True
                else: 
                    dp[1] = False
                    #return False
            else:
                substr = s[:i]
                for j in range(len(substr)):
                    subsubstr = substr[j:]
                    #print subsubstr
                    if subsubstr in wordDict and dp[j] == True:
                        dp[i] = True
                        break
                    else:
                        dp[i] = False
            #print substr, i, dp[i], dp[i-1]
                
        return dp[len(s)] 
```

