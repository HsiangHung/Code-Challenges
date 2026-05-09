#  5. Longest Palindromic Substring (medium)
#  https://leetcode.com/problems/longest-palindromic-substring/
#  Microsoft, Amazon, Bloomberg
#
#  use, if a Palindrome string is s[i:j], check if s[i-1] + s[i:j] + s[j] is Palindrome
# 
class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""

        def sliding_check(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        l, r = 0, 0
        max_palindrome = 0
        for i in range(len(s)):
            
            len1 = sliding_check(i, i+1) # "babad", sart from "b", and -1, + 1
            len2 = sliding_check(i, i) # "cbbd", start from "bb" and -1, +1

            palind_len = max(len1, len2)

            if palind_len > max_palindrome:
                max_palindrome = palind_len
                l = i - (palind_len - 1) // 2
                r = i + palind_len // 2

        return s[l:r+1]
        