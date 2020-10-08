# [#392] Is Subsequence
# 
#  Pinterest
#
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "": return True
        
        i, j = 0, 0
        while i <= len(s)-1 and j <= len(t)-1:
            if s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
                
        if i != len(s): return False
        return True
       