## [Leetcode#67] Add Binary
##
## with a prepared binary array binary_sum = [0,0,..0] 
##
class Solution(object):
    def addBinary(self, a, b):
        """
          1111
        +   11
         -----
         10010  

         x+y = 3 => 11
         x+y = 2 => 10
         x+y = 1 => 01
         x+y = 0 => 00
        """

        a_,  b_ = list(a)[::-1], list(b)[::-1]

        res = []
        i, j = 0, 0
        next_digit = 0
        while i < len(a) or j < len(b):
            x, y = a_[i] if i < len(a) else 0, b_[j] if j < len(b) else 0

            binary_sum = int(x) + int(y) + next_digit
            
            res.append(binary_sum % 2)
            next_digit = binary_sum // 2

            i += 1
            j += 1
        
        if next_digit == 1:
            res.append(1)

        return "".join([str(x) for x in res[::-1]])