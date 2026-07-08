# 1400. Construct K Palindrome Strings
#
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        '''
        to form a palindrome, not allow odd number of letters > k.
        '''
        if k > len(s): return False
        
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
            
        num_odds = 0
        for char in s_dict:
            if s_dict[char] % 2 == 1:
                num_odds += 1
                if num_odds > k: return False
        
        return True