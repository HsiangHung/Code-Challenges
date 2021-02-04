#  139. Word Break (medium)
#  https://leetcode.com/problems/word-break/
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        http://bangbingsyb.blogspot.com/2014/11/leetcode-word-break-i-ii.html
        https://baihuqian.github.io/2018-06-24-word-break/
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


## NOTE: using the following BFS solution cannot pass all test cases. Time exceed. 

class BFSSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        queue = [""]
        
        while queue:
            word1 = queue.pop(0)
            if word1 == s: return True
            
            for word2 in wordDict:
                if s[len(word1) : len(word1)+len(word2)] == word2:
                    queue.append(word1+word2)
             
        return False
                    
