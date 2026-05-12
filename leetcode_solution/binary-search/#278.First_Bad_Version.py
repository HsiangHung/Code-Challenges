#  278. First Bad Version (easy)
#  https://leetcode.com/problems/first-bad-version/
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return n
        return self.search(n, )
        
    def search(self, n, offset):
        '''
        offset term is to calibrate the value.
        '''
        if n == 1 or n == 0: return 1
        
        m = n // 2
        a, b = isBadVersion(m+offset), isBadVersion(m+1+offset)
        
        if not a and b:
            return m+1+offset
        elif a and b:
            return self.search(m, offset)
        else:
            return self.search(n-m, offset+m)
        