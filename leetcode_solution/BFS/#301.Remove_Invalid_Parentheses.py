# 301. Remove Invalid Parentheses (hard)
# https://leetcode.com/problems/remove-invalid-parentheses/
#
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        BFS Reference:
        http://bookshadow.com/weblog/2015/11/05/leetcode-remove-invalid-parentheses/
        https://yeqiuquan.blogspot.com/2017/05/301-remove-invalid-parentheses.html

        initalize a queue, e.g. s = "()())", queue = ["()())"], 
            done_BFS = False 
            (1) s = queue.pop(0) = "()())", queue = []
                s is not valid, so next to try all comintations one paraenthese less
                queue = [")())"]
                queue = [")())", "(())"]
                queue = [")())", "(())", "()))"]
                queue = [")())", "(())", "()))", "()()"]
                queue = [")())", "(())", "()))", "()()", "()()"]
            (2) s = queue.pop(0) = ")())", queue = ["(())", "()))", "()()", "()()"]
                s is not valid, so next to try all comintations one paraenthese less
                queue = ["(())", "()))", "()()", "()()", "())"]
                queue = ["(())", "()))", "()()", "()()", "())", ")))"]
                queue = ["(())", "()))", "()()", "()()", "())", ")))", ")()"]
                queue = ["(())", "()))", "()()", "()()", "())", ")))", ")()", ")()"]
            (3) s = queue.pop(0) = "(())", queue = ["()))", "()()", "()()", "())", ")))", ")()", ")()"]
                s is valid, so no need to try one paraenthese less comintations

                * done_BFS = True, so the minimum valid parentheses must happen four parentheses
                output = ["(())"]

            (4) s = queue.pop(0) = "()))", queue = ["()()", "()()", "())", ")))", ")()", ")()"]
                s is not valid, but done_BFS = True, no need to try one paraenthese less comintations
       
            (5) s = queue.pop(0) = "()()", queue = ["()()", "())", ")))", ")()", ")()"]
                s is valid, but done_BFS = True, no need to try one paraenthese less comintations
            
            .....
        '''
        output = []
        visited = set({})
        done = False
        
        queue = [s]
        while queue:
            s = queue.pop(0)
            if self.isValid(s):
                output.append(s)
                done_BFS = True
            
            if not done_BFS:
                for i in range(len(s)):
                    if s[i] in ["(", ")"]:
                        new_s = s[:i] + s[i+1:]
                        if new_s not in visited:
                            visited.add(new_s)
                            queue.append(new_s)

        return output

    
    def isValid(self, s):
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0 or stack[-1] == ")": return False
                stack.pop()
        return len(stack) == 0