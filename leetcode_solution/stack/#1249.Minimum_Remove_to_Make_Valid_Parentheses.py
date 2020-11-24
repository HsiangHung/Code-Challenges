#  1249. Minimum Remove to Make Valid Parentheses (medium)
#  https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
#
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        The trick here is we store all "(" and ")" position indices, and 
        if only if "(" + ")" we pop stack and index array. The remaining indices are 
        invalid paraenthese needed to remove.
        '''
        stack = []
        idx = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == ")":
                if len(stack) == 0:
                    idx.append(i)
                    stack.append(s[i])
                else:
                    if stack[-1] == "(" and s[i] == ")":
                        stack.pop()
                        idx.pop()
                    else:
                        stack.append(s[i])
                        idx.append(i)
                            
        return "".join([s[i] for i in range(len(s)) if i not in set(idx)])