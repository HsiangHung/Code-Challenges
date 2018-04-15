# [#5] Longest Palindromic Substring
# 
#  Microsoft, Amazon, Bloomberg
#
#  use, if a Palindrome string is s[i:j], check if s[i-1] + s[i:j] + s[j] is Palindrome
# 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        
        dp ={1: [(i,i) for i in range(len(s))], 2: [(i, i+1) for i in range(len(s)-1) if s[i] == s[i+1]]}

        max_palindrome = 1
        if len(dp[2]) > 0: max_palindrome = 2
        
        len_substring = 3
        noPalindrome = 0   
        ## when two consective substring len shows no Palindrome, we can leave the loop.
        ## e.g. if len = 10, there is no Palindrome, then len = 12 no need to check
        ##      if len = 11, there is no Palindrome, then len = 13 no need to check
        ##      then even string has length of 100, longest palindrome is 9.
        while len_substring <= len(s) and noPalindrome < 2:
            
            dp[len_substring] = []
            for sub_index in dp[len_substring-2]:
                i, j = sub_index
                if i > 0 and j < len(s)-1 and s[i-1] == s[j+1]:
                    dp[len_substring].append((i-1, j+1))
                                
            if len(dp[len_substring]) > 0: 
                max_palindrome = len_substring
                noPalindrome = 0
            else:
                noPalindrome += 1
                
            len_substring += 1
                
        return s[dp[max_palindrome][0][0]: dp[max_palindrome][0][1]+1]