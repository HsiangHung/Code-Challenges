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
        
        stack, idx = [], []  # idx store invalid parathese 
        for i, char in enumerate(s):
            if char == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
                idx.pop()
            else:
                stack.append(char)
                idx.append(i)
        
        # run through entire string to know the index of invalid parethese.
        # e.g. ")())()", the only invalid index is idx = [0, 3]. Then we sweep the string again to see
        # longest string between any two indices.
        
        if len(idx) == 0: # if empty stack, meaning no invalid parenthesis, and entire s is valid.
            return len(s) 
        else:
            if len(idx) == 1: # if len(idx) == 1, one invalid parathese, say "()((())", idx = [2]
                return max(idx[0], len(s)-(idx[0]+1)) 
            else:
                # e.g. if len(s) = 11, idx = [3, 6], then valid are [0,1,2], [4,5], [7,8,9,10]. return 4
                max_len = idx[0]  
                for i in range(1, len(idx)):
                    max_len = max(max_len, idx[i]-idx[i-1]-1)

            return max(max_len, len(s)-(idx[i]+1))
  

                   