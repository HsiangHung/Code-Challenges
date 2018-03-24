# [#28] Implement strStr()
#
# 
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_needle = len(needle)
        
        if len(haystack) < n_needle: return -1
        
        for i in range(len(haystack)-n_needle+1):
            if self.isOccurrence(haystack[i:i+n_needle], needle):
                return i
            
        return -1
            
            
            
    def isOccurrence(self, subhaystack, needle):
        for i in range(len(needle)):
            if subhaystack[i] != needle[i]:
                return False
        return True
                