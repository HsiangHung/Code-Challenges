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

        def single_multi(n1, n2):
            "n2 is a single digit"
            multi = ""
            next_digit = 0
            for i in range(len(n1)-1, -1, -1):
                res = int(n1[i]) * int(n2) + next_digit
                next_digit, r = res // 10, res % 10
                multi = str(r) + multi
            return str(next_digit) + multi if next_digit != 0 else multi

        memory = {} 
        # at most only 10 keys in this dict to speed up calculation

        ans = 0
        d = 1
        for i in range(len(num2)-1, -1, -1):
            if num2[i] not in memory:
                sub_multi = int(single_multi(num1, num2[i]))
                memory[num2[i]] = sub_multi

            ans += memory[num2[i]] * d
            d *= 10

        return str(ans)
        