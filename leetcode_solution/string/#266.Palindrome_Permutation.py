#  266. Palindrome Permutation (easy)
#  https://leetcode.com/problems/palindrome-permutation/
#
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) <= 1: return True
        
        char_dict = {}
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
            
        num_odd = 0
        for char in char_dict:
            if char_dict[char] % 2 == 1:
                num_odd += 1
            
            if num_odd >= 2: return False
            
        return True