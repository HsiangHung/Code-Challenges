## [#125] Valid Palindrome
#   
#  zenefit, Facebook, Uber, Microsoft
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha = set({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',           
                     'r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'})
        
        left, right = 0, len(s)-1
        while left < right:
            left_ch = s[left].lower()
            right_ch = s[right].lower()
            if left_ch in alpha and right_ch in alpha:
                if left_ch != right_ch:
                    return False
                else:
                    left += 1
                    right -= 1
            elif left_ch in alpha and right_ch not in alpha:
                right -= 1
            elif left_ch not in alpha and right_ch in alpha:
                left += 1
            else:
                left += 1
                right -= 1 
                
        return True