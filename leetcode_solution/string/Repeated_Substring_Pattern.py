## [Leetcode#459] Repeated Substring Pattern
##
##  slide checking: if abcabcabc = abc + abc + abc
##
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        for i in range(1,len(str)):
            substr = str[:i]
            if len(str) % len(substr) == 0:
                r = int(len(str)/len(substr))
                n = len(substr)
                isMultiple = True
                for i in range(1, r):
                    check_str = str[i*n:(i+1)*n]
                    if check_str != substr: isMultiple = False
                if isMultiple == True: return isMultiple
        return False