#  139. Word Break (medium)
#  https://leetcode.com/problems/word-break/
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        http://bangbingsyb.blogspot.com/2014/11/leetcode-word-break-i-ii.html
        https://baihuqian.github.io/2018-06-24-word-break/
        if s is breakable, s[k:] is in dictionary and s[j:k] is in dict .... and s[0:j] is in

        e.g.
        s = "leetcode",  wordDict = ["leet", "code"]
        dp[0] = True   (base case: empty string)
        dp[1] = False  (no word ends at index 1)
        dp[2] = False
        dp[3] = False
        dp[4] = True   ← dp[0]=T and s[0:4]="leet" ∈ dict
        dp[5] = False
        dp[6] = False
        dp[7] = False
        dp[8] = True   ← dp[4]=T and s[4:8]="code" ∈ dict  ✓
        """

        word_dict = set(wordDict)

        dp = [False] * (len(s) + 1) 
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(i+1, len(s) + 1):
                if s[i:j] in word_dict and dp[i] is True:
                    print(i, j, s[i:j])
                    dp[j] = True
        
        return dp[len(s)]


## NOTE: using the following BFS solution cannot pass all test cases. Time exceed. 
#
# class BFSSolution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         queue = [""]
#         while queue:
#             word1 = queue.pop(0)
#             if word1 == s: return True
#            
#             for word2 in wordDict:
#                 if s[len(word1) : len(word1)+len(word2)] == word2:
#                     queue.append(word1+word2)
#             
#         return False
                    
