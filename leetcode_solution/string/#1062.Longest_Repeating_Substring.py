#  1062. Longest Repeating Substring (medium)
#  https://leetcode.com/problems/longest-repeating-substring/
#
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        '''
        check substring length from len(S)-1 (a whole string impossible to repeat)
        and grafually decrease until substring length = 1.
        '''
        sub_len = len(S) - 1
        while sub_len > 0:
            
            repeat = set({})
            
            i = 0
            while i+sub_len <= len(S):
                if S[i: i+sub_len] in repeat: return sub_len
                repeat.add(S[i: i+sub_len])
                i += 1
            
            sub_len -= 1
            
        return sub_len
    