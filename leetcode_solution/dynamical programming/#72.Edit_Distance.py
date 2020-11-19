# 72. Edit Distance (hard)
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        * Youtube: https://www.youtube.com/watch?v=fN3Js7H72HE&list=PLQiyVNMpDLKnZYBTUOlSI9mi9wAErFtFm&index=8
        * ButtomDown code but time limit exceed: 
         https://www.geeksforgeeks.org/edit-distance-dp-5/
        '''
        
        if word1 == word2 == "": return 0
        if word1 == "":
            return len(word2)
        elif word2 == "":
            return len(word1)
        
        dp = [[0]+[i+1 for i in range(len(word1))]]
        for j in range(1, len(word2)+1):
            dp.append([j]+[0]*(len(word1)))
                                
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                # print (i, j)
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    
        return dp[len(word2)][len(word1)]



class Solution2:
    '''
    This resurson version has time limit exceed issues.
    But it is easier to understand the algorithm.
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "" and word2 == "": return 0
    
        if word1 == "": 
            return len(word2)
        elif word2 == "":
            return len(word1)
    
        return self.ButtonDown(word1, word2, len(word1), len(word2))
    
    def ButtonDown(self, s1, s2, m, n):
        
        if m == 0: return n
        if n == 0: return m
        
        if s1[m-1] == s2[n-1]:
            return self.ButtonDown(s1, s2, m-1, n-1)
        
        return 1 + min(self.ButtonDown(s1, s2, m-1, n), 
                       self.ButtonDown(s1, s2, m, n-1),
                       self.ButtonDown(s1, s2, m-1, n-1))
        
        