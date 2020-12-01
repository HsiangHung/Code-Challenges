#  3. Longest Substring Without Repeating Characters (medium)
#  https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Use double index to run through the string and save letter set
        if there is repeated letted, moving i until see s[j]
        
        e.g. s = "pwwkew"
        i  j  letter_set          max_len
        0  0  {"p"}                 1
        0  1  {"p", "w"}            2
        2  2  {"p", "w", "w"}       2  => {"w"}
        2  3  {"w", "k"}            2
        2  4  {"w", "k", "e"}       3
        2  5  {"w", "k", "e", "w"}  3  => {k", "e", "w"}
        '''
        if len(s) <= 1: return len(s)
        
        letter_set = {s[0]}
        
        max_len = 1
        
        i, j = 0, 1
        while j < len(s) and i < len(s):
            if s[j] not in letter_set:
                letter_set.add(s[j])
                max_len = max(max_len, len(letter_set))
            else:
                while s[i] != s[j]:
                    letter_set.remove(s[i])
                    i += 1
                i += 1                
            j += 1
                
        return max_len
                