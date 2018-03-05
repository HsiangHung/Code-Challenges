# [#434] Number of Segments in a String
#
#
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        
        if s[0] == " ":
            num_segment = 0
        else:
            num_segment = 1
        
        for i in range(1, len(s)):
            if s[i] != " " and s[i-1] == " ":
                num_segment += 1
                
        return num_segment