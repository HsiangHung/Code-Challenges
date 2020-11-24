#  20. Valid Parentheses (easy)
#  https://leetcode.com/problems/valid-parentheses/
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        para_dict = {"}":"{", "]": "[", ")": "("}
        
        stack = []
        for para in s:
            if len(stack) == 0:
                stack.append(para)
            else:
                if para in para_dict:
                    ch = stack.pop()
                    if ch != para_dict[para]:
                        return False
                else:
                    stack.append(para)
                    
        return len(stack) == 0
        