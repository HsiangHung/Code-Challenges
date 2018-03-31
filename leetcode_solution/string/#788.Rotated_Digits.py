# [#788] Rotated Digits
#
#
#
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num_good = 0
        for x in range(N+1):
            x = set(list(str(x)))
            if '7' not in x and '3' not in x and '4' not in x:
                if '2' in x or '5' in x or '6' in x or '9' in x:
                    num_good += 1
                    
        return num_good
        