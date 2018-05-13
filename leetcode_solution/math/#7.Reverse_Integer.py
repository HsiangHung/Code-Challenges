## [Leetcode#7] Reverse Integer
#   
#  Bloomberg, Applt
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10: return x
        if x > 2**31-1 or x < -2**31: return 0
        
        sgn = x/abs(x)
        
        rev_num = int(''.join([str(digit) for digit in self.get_digits(abs(x))]))
        if rev_num > 2**31-1 or rev_num < -2**31: return 0
        return sgn*rev_num
        
    def get_digits(self, x):
        if x < 10: return [x]
        digits = [x % 10]
        if x // 10 != 0:
            return digits + self.get_digits(x//10)
        else:
            return digits