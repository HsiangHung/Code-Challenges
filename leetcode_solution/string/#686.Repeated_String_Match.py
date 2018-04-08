# [#686] Repeated String Match
#
#   google 
#
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        ## if len of A > len of B: check
        if len(A) >= len(B):
            if self.isSubstring(A, B): return 1
        
        cnt = 1
        string = A
        while len(string) < len(B):
            string += A
            cnt += 1

        # if len of A >= len of B, check again
        if self.isSubstring(string, B): return cnt
            
        # like the example, if nothing matches, add one more and check, if none, return -1
        string += A
        cnt += 1
        if self.isSubstring(string, B): return cnt
        
        return -1
    
    def isSubstring(self, string, substring):
        if string == substring: return True
        for i in range(len(string)-len(substring)+1):
            if string[i: i+len(substring)] == substring:
                return True
        return False