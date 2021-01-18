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
        for i, char in enumerate(s):
            if char == "(":
                stack.append((i, "("))
            elif char == ")":
                if len(stack) > 0 and stack[-1][1] == "(":
                    stack.pop()
                else:
                    stack.append((i, ")"))
        
        stack = set([i[0] for i in stack])
        return "".join([s[i] for i in range(len(s)) if i not in stack])