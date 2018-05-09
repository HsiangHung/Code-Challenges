## [Leetcode#242] Valid Anagram
##
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        
        for i in range(len(t)):
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
            
        if len(s_dict.keys()) != len(t_dict.keys()): return False
        
        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False
            
        return True
        