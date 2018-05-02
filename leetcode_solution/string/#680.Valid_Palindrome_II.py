# [#680] Valid Palindrome II
#
#
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        isInvalid = False
        while i < j:
            #print i, s[i], j, s[j]
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:         
                substringValid = False
                ## in the following we need to check two cases, either move i, or move j
                ## ie. "lcupuu..... uupucul"
                ##  both s[i] == s[j-1] and s[i+1] == s[j] satisfy
                if s[i] == s[j-1]:
                    substringValid = substringValid or self.validPalindrome2(s[i:j])
                    
                if s[i+1] == s[j]:
                    substringValid = substringValid or self.validPalindrome2(s[i+1:j+1])
                    
                if substringValid: 
                    return True
                else:
                    return False
                
        return True
        
        
    def validPalindrome2(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
                
        return True