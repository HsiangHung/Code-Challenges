#  43. Multiply Strings (medium)
#  https://leetcode.com/problems/multiply-strings/
#
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        idea: https://www.geeksforgeeks.org/dsa/multiply-large-numbers-represented-as-strings/

               123
             x 456
            -------
               738
              615
             493

        so during process, only left shift one digit, and keep rightmost digits, and contact finally.
        """
        if num1 == "0" or num2 == "0": 
            return "0"

        num1 = int(num1)
        res = 0
        rightmost_digit = []
        for i, x in enumerate(list(num2)[::-1]): # e.g. "456" -> ["6", "5", "4"]

            multilication = num1 * int(x)

            if i == 0:
                res = str(multilication)
            else:
                if int(res) < 10:
                    res = "0" + res
                rightmost_digit.insert(0, res[-1])
                res = str(int(res[:-1]) + multilication)

        return res + "".join(rightmost_digit)
