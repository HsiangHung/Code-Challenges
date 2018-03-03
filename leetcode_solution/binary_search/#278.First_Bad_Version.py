# [#278] First Bad Version
#
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
        return self.search(0, n)
        
    def search(self, init, n):
        
        if n-init == 1:
            if isBadVersion(init+1):
                return init+1
            else:
                return init+2            
        
        mid = (n-init) // 2 + 1 + init
                
        isMidBad = isBadVersion(mid)
        isMidBad2 = isBadVersion(mid-1)
        
        if n-init == 2:
            if isMidBad and not isMidBad2:
                return init+2
            elif isMidBad2:
                return init+1
            elif not isMidBad:
                return init+2
        
        if isMidBad and not isMidBad2:
            return mid
        elif isMidBad2:
            return self.search(init, mid-2)
        elif not isMidBad:
            return self.search(mid, n)
        
        