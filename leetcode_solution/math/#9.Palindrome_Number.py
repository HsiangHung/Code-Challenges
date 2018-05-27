## [#9] Palindrome Number
#   
#  
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        
        num = x
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10

        left, right = 0, len(digits)-1
        while left < right:
            if digits[left] != digits[right]:
                return False
            left += 1
            right -=1
            
        return True