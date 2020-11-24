#  227. Basic Calculator II (medium)
#  https://leetcode.com/problems/basic-calculator-ii/
#
class Solution:
    def calculate(self, s: str) -> int:
        '''
        use stack, first run through to implement all muplitication and division
        and then the remaining stack is only ["+", and "-"]
        At the beginning, remove all space " " is more convenient. 
        As long as we met operators "*" or "/", look for previous element in stack and 
        search numbers behind the operators.
        '''
        s = [char for char in s if char != " "]
        
        nums = set([str(i) for i in range(10)])
        operators = set(["+", "-", "*", "/"])
        
        stack = []
        i = 0
        while i < len(s):
            if s[i] in nums: # e.g. incoming s[i] = "1"
                if len(stack) > 0 and stack[-1] not in operators: # e.g. [.."2"] => [.."21"]
                    num = stack.pop()
                    stack.append(num+s[i])
                else:
                    stack.append(s[i])
            elif s[i] in ("*", "/"):
                x, op = stack.pop(), s[i]
                y = ""
                while i+1 <= len(s)-1 and s[i+1] in nums:
                    y += s[i+1]
                    i += 1
                stack.append(str(self.operation(op, x, y)))
            else:
                if s[i] != " ": stack.append(s[i])
            i += 1
        
        ans = int(stack[0])
        for i in range(1, len(stack), 2):
            if stack[i] == "+":
                ans += int(stack[i+1])
            elif stack[i] == "-":
                ans -= int(stack[i+1])

        return ans
                
        
    def operation(self, op, x, y):
        if op == "*":
            return str(int(x) * int(y))
        elif op == "/":
            return str(int(x) // int(y))
        
