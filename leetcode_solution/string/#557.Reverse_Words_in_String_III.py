## [Leetcode#557] Reverse Words in a String III
##
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = ""
        s = s.lstrip().rstrip().split(" ")
        for substring in s:
            reverse += substring[::-1] + " "
            
        return reverse.rstrip()