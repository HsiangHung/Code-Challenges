#  516. Longest Palindromic Subsequence (medium)
#  https://leetcode.com/problems/longest-palindromic-subsequence/
#
class Solution:
    '''
     https://www.youtube.com/watch?v=_nCsPn7_OgI
     http://bookshadow.com/weblog/2017/02/12/leetcode-longest-palindromic-subsequence/
     
                             j\i 0 1 2 3 4
         b b b a b               b b b a b
       b 1                   0 b 1 2 3 3 4
       b 0 1            =>   1 b 0 1 2 2 3
       b   0 1               2 b   0 1 1 3
       a     0 1             3 a     0 1 1
       b       0 1           4 b       0 1
       
    diagonal all 1, and 
    * if s[i] == s[j] then dp[i,j] = dp[i-1, j+1] + 2, else max(dp[i-1, j+1], dp[i-1,j], dp[i, j+1])
      where len(s[i:j+1]) = l for dp[i,j], then l-2 for dp[i-1, j+1]
       
    '''
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == "": return 0

        dp = []
        for _ in range(len(s)):
            dp.append([0]*len(s))
            
        for i in range(len(s)):
            dp[i][i] = 1
            
        max_dp = 1
        
        l = 1
        while l <= len(s)-1:
            j = 0
            while j + l <= len(s)-1:
                if s[j] == s[j+l]:
                    dp[j][j+l] = dp[j+1][j+l-1] + 2
                else:
                    dp[j][j+l] = max(dp[j+1][j+l], dp[j][j+l-1])
                    
                max_dp = max(max_dp, dp[j][j+l])
                j += 1
            
            l += 1
        

        return max_dp