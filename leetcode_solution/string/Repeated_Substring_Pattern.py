## [Leetcode#459] Repeated Substring Pattern
##
##  if 'abcabcabc' is multiple of 'abc'?
##   check 'abc abc abc' for substring of 'abc'
##
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        n = len(str)
        for i in range(1,int(len(str)/2)+1):
            substr = str[:i]
            if n % i ==0:
                r = int(n/i)
                isRepeat = True
                start = i
                end = 2*i
                for j in range(1,r):
                    if str[start:end] != substr: isRepeat = False
                    start += i
                    end += i
                if isRepeat == True: return True
        return False