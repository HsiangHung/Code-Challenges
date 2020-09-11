# #32. Longest Valid Parentheses
#
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        NOTE we need to find "longest valid (well-formed) parentheses substring"
        if s = "()(()", it is 2, not 4. "(()())" = "((()))" = 6
        "(()()" = 4
        
        We save site indices for valid paretheses. If paretheses are not in sequence, 
        site indices won't continue.
        '''
        
        if len(s) <= 1: return 0
        
        stack = []
        
        valid_pare = []
        for i in range(len(s)):
            if stack == []:
                stack.append((s[i], i))
            else:
                if stack[-1][0] == "(" and s[i] == ")":
                    valid_pare += [stack[-1][1], i]
                    stack.pop()
                else:
                    stack.append((s[i], i))
        
        valid_pare = sorted(valid_pare) ## this is critical
        
        # print (valid_pare)
                
        if len(valid_pare) > 0:
            valid_len, longest = 1, 0
            for i in range(1, len(valid_pare)):
                if valid_pare[i] != valid_pare[i-1]+1:
                    valid_len = 1
                else:
                    valid_len += 1
                longest = max(longest, valid_len)

            return longest
        else:
            # consider "((" or ")(" etc.
            return 0
 