#  227. Basic Calculator II (medium)
#  https://leetcode.com/problems/basic-calculator-ii/
#
class Solution:
    def calculate(self, s: str) -> int:
        class Solution:
    def calculate(self, s: str) -> int:
        """
        This code has three parts:
        1. first deal with numbers > 10, need to concat num char. "14" != ["1", "4"]
        2. deal with "*" and "/" operations.
        3. deal with "+" and "-" operations and get answer
        """

        num_set = set([str(x) for x in range(10)])

        # 1. deal with numbers > 10, e.g. "140/30 + 2" -> ["140", "/", "30", "+", "2"]
        stack = []
        i = 0
        while i < len(s):
            char = s[i]
            if char != " ":
                if char not in num_set:
                    stack.append(char) # "+", "-", "*", "/" operations
                else:
                    j = i + 1
                    while j < len(s) and s[j] in num_set:
                        char += s[j] 
                        j += 1
                    stack.append(char)
                    i = j - 1
            i += 1
    
        # 2. deal with "*" and "/" first. e.g. ["14","/","3","-","2"] -> ["4", "-", "2"]
        i = 0
        while i < len(stack):
            # print(i, stack[i])
            if stack[i] in ("*", "/"):
                op = stack.pop(i)
                num2 = int(stack.pop(i))
                num1 = int(stack.pop(i-1))
                if op == "*":
                    stack.insert(i-1, str(num1 * num2))
                else: # if op = "/"
                    stack.insert(i-1, str(int(num1 / num2)))
            else:
                i += 1

        
        # 3. deal with "+" and "-", e.g. ["3", "+", "2"] => 3 + 2
        i, res = len(stack)-1, 0
        prev_ch = ""
        while i >= 0:
            # print(i, stack[i], res)
            if stack[i] not in ("+", "-"):
                char = str(stack[i]) + prev_ch
                prev_ch = char
            else:
                op = stack[i]
                if op == "+":
                    res += int(char)
                else:
                    res -= int(char)
                prev_ch = ""
    
            i -= 1

        return res + int(char)
