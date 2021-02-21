#  5. Longest Palindromic Substring (medium)
#  https://leetcode.com/problems/longest-palindromic-substring/
#
#  Microsoft, Amazon, Bloomberg
# 
class Solution(object):
    '''
    if a Palindrome string is s[i:j], check if s[i-1] + s[i:j] + s[j] is Palindrome
    each len_substring, check if dp[len_substring-2] exist. 
    if both dp[len_substring-1] and dp[len_substring-2] not exist, no need continue search
    '''
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2: return s
        
        dp ={1: [(i,i) for i in range(len(s))], 2: [(i, i+1) for i in range(len(s)-1) if s[i] == s[i+1]]}

        max_palindrome = 2 if len(dp[2]) > 0 else 1
        
        len_substring = 3
        search = True   
        ## when two consective substring len shows no Palindrome, we can leave the loop.
        ## e.g. if len = 10, there is no Palindrome, then len = 12 no need to check
        ##      if len = 11, there is no Palindrome, then len = 13 no need to check
        ##      then even string has length of 100, longest palindrome is 9.
        while len_substring <= len(s) and search:
            if len_substring -2 in dp:
                dp[len_substring] = []
                for i in range(len(dp[len_substring-2])):
                    idx1, idx2 = dp[len_substring-2][i]

                    if idx1 >= 1 and idx2 < len(s)-1 and s[idx1-1] == s[idx2+1]:
                        dp[len_substring].append((idx1-1, idx2+1))
                        max_palindrome = max(max_palindrome, len_substring)
            
            if len_substring - 1 not in dp and len_substring-2 not in dp: search = False
            len_substring += 1
                
        return s[dp[max_palindrome][0][0]: dp[max_palindrome][0][1]+1]