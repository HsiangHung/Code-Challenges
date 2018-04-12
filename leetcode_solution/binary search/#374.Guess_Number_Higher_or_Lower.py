# [#374] Guess Number Higher or Lower
#
#   google
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return n
        
        start, end = 1, n
        while end - start != 0:
            mid = (end - start + 1)//2 + start
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                end = mid - 1
            elif ans == 1:
                start = mid + 1

        return end