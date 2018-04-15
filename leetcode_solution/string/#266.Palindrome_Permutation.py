# [#266] Palindrome Permutation
#
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ch_dict = {}
        for ch in s:
            ch_dict[ch] = ch_dict.get(ch, 0) + 1
        
        num_odd = 0
        for ch in ch_dict:
            if ch_dict[ch] % 2 == 1:
                num_odd += 1
                
        if len(s) % 2 == 0 and num_odd == 0:
            return True
        elif len(s) % 2 == 1 and num_odd == 1:
            return True
        
        return False