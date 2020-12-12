#  32. Longest Valid Parentheses (hard)
#  https://leetcode.com/problems/longest-valid-parentheses/
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
        
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            else:
                if len(stack) > 0 and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((s[i], i))  # save stack as (s[i], index)
        

        # run through entire string to know the index of invalid parethese.
        # e.g. ")())()", the only invalid is [0, 3]. Then we sweep the string again to see
        # longest string between any two indices.
        
        if len(stack) > 0:
            index = [x[1] for x in stack]
            i, j = 0, 0
            max_pare = 0
            while len(index) > 0 and j <= len(index)-1:
                max_pare = max(max_pare, index[j] - i)
                i = index[j] + 1
                j += 1

            if index[-1] != len(s)-1: max_pare = max(max_pare, (len(s)-1)-index[-1])
            return max_pare
        else:    # if empty stack, meaning no invalid parenthesis, and entire s is valid.
            return len(s)
            