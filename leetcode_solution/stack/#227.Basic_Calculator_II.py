#  227. Basic Calculator II (medium)
#  https://leetcode.com/problems/basic-calculator-ii/
#
class Solution:
    def calculate(self, s: str) -> int:
        """
        ref: https://www.youtube.com/watch?v=G2AZJDkh6_E
        e.g. s = "33 + 6*4/2-5"
        s = ["3", "3", "+", "6", "*", "4", "/", "2", "-", "5"] + ["+"]

         ch  num   last_op        stack
              ""      "+"         []
        "3"   "3"     "+"         []
        "3"  "33"     "+"         []
        "+"   ""      "+"         [33]
        "6"   "6"     "+"         [33]
        "*"   ""      "+" -> "*"  [33,6]
        "4"   "4"     "*"         [33,6] 
        "/"   ""      "*" -> "/"  [33,6] -> [33], 6*4=24 -> [33,24] 
        "2"   "2"     "/"         [33,24] 
        "-"   ""      "/" -> "-"  [33,24] -> [33], 24/2 -> [33,12]    
        "5"   "5"     "-"         [33,12]
        "+"   ""      "-" -> "+"  [33,12] + [-5] 
                                  [33,12,-5]
        """
        s = [x for x in list(s) if x != " "]
        s.append("+") # IMPORTANT! forces the last number to flush at the end

        stack = []
        num = ""
        last_op = "+"
        for ch in s:
            if ch not in ("+", "-", "*", "/"): # continguous number, e.g. "123"
                num += ch
            else:  # now, be "+", "-", "*", "/"

                n = int(num)
                if last_op == "+":
                    stack.append(n)
                elif last_op == "-":
                    stack.append(-n)
                elif last_op == "*":
                    stack.append(stack.pop()*n)
                else:
                    stack.append(int(stack.pop()/n))
                
                last_op = ch
                num = ""
            
        return sum(stack)
