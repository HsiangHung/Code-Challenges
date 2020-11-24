#  150. Evaluate Reverse Polish Notation (medium)
#  https://leetcode.com/problems/evaluate-reverse-polish-notation/
#
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ("+", "-", "*", "/")
        
        stack = []
        for x in tokens:
            if x not in operators:
                stack.append(x)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.operation(a, b, x))
        
        return int(stack[-1])
                
                
    def operation(self, a, b, operation):
        if operation == "+":
            return int(a) + int(b)
        elif operation == "-":
            return int(a) - int(b)
        elif operation == "*":
            return int(a) * int(b)
        else:
            return int(a) / int(b)