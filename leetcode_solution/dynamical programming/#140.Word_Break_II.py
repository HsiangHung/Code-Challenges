#  140. Word Break II (hard)
#  https://leetcode.com/problems/word-break-ii/
#
class Solution:
    '''
    in addition to the dp = {True, False}, need to store the next pointer.
        e.g. s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]
        
        we got dp = [True, False, False, True, True, False, False, True, False, False, True]
                
        If dp[-1] = False, return [], otherwise we move to collect answer:
        
        now dp starts as dp = {0: [""]}.
        e.g. s = "catsanddog",
             wordDict = ["cat", "cats", "and", "sand", "dog"]             
        then we will have same iteration to get dp
        dp = {0: [''], 3: [' cat'], 4: [' cats'], 7: [' cat sand', ' cats and'], 
             10: [' cat sand dog', ' cats and dog']}
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        
        dp = [False]*(len(s)+1)
        dp[0] = True

        # check if there is solution:
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and dp[i]:
                    dp[j] = True
        
        if not dp[len(s)]:
            return []
        else:        
            dp = {0: [""]}
            for i in range(len(s)+1):
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict and i in dp:
                        for x in dp[i]:
                            dp[j] = dp.get(j, []) + [x+" "+s[i:j]]
        
            return [x[1:] for x in dp[len(s)]] if len(s) in dp else []
      
        