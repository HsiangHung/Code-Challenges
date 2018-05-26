## [#258] Add Digits
#   
#  Adobe
#
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10: return num
        
        num = sum([int(x) for x in str(num)])
        
        return self.addDigits(num)