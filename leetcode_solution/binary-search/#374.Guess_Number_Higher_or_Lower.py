#
#  374. Guess Number Higher or Lower
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        if n == 1:
            return n

        start, end = 1, n
        while end - start > 0:

            if guess(end) == 0:
                return end

            if guess(start) == 0:
                return start

            mid = (end - start) // 2 + start
            resp = guess(mid)
            if resp == 0:
                return mid
            elif resp == -1:
                end = mid
            else:
                start = mid
        