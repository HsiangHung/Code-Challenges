# [#342] Power of Four
#
# 2-sigma
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0: return False
        
        return self.bit(num) == 1
        
        
    def bit(self, num):
        if num < 4:
            return num % 4
        
        return self.bit(num//4) + (num % 4)