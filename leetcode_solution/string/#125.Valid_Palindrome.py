## [Leetcode#125] Valid Palindrome
##
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import copy
        
        if len(s) <= 1: return True
        
        alphanumeric = set({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'})
                    
        alphanumeric2 = copy.copy(alphanumeric)
        for ch in alphanumeric2:
            alphanumeric.add(ch.upper())
        
        for i in range(10):
            alphanumeric.add(str(i))
            
            
        isPali = True
        i = 0
        j = len(s)-1
        while j>=i:
            s1 = s[i]
            s2 = s[j]
            if s1 in alphanumeric and s2 in alphanumeric:
                s1 = s1.lower()
                s2 = s2.lower()
                if s1 != s2: return False
                i +=1
                j -=1
            elif s1 in alphanumeric and s2 not in alphanumeric:
                s1 = s1.lower()
                j -=1
            elif s1 not in alphanumeric and s2 in alphanumeric:
                s2 = s2.lower()
                i +=1
            else:
                i +=1
                j -=1
                
        return isPali