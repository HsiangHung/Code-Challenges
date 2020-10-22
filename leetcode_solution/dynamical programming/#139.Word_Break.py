# # 139. Word Break
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        if s is breakable, s[k:] is in dictionary and s[j:k] is in dict .... and s[0:j] is in
        '''
        wordDict = set(wordDict)
                
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and dp[i]:
                    dp[j] = True
                        
        return dp[-1]
                    
