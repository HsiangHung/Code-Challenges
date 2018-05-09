## [Leetcode#290] Word Pattern
##
##
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(" ")
        if len(str) != len(pattern): return False
        
        ## notice the case
        ## "abba", "dog dog dog dog"
        
        str_dict, str_set = {}, set({})
        for i in range(len(pattern)):
            ch = pattern[i]
            if ch not in str_dict:
                str_dict[ch] = str[i]
                if str[i] in str_set:
                    return False
                else:
                    str_set.add(str[i])
            else:
                if str[i] != str_dict[ch]:
                    return False
                
        return True

                