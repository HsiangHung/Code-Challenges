#  277. Find the Celebrity (medium)
#  https://leetcode.com/problems/find-the-celebrity/
#
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    '''
    knows(A, B) = True:  then B may be celebrity, and A must not
    knows(A, B) = False: then B must not be celebrity
    https://zhongwen.gitbook.io/leetcode-report/medium/277.-find-the-celebrity
    https://www.cnblogs.com/grandyang/p/5310649.html (sol3)
    '''
    def findCelebrity(self, n: int) -> int:
        
        res = 0
        for i in range(1, n):
            if knows(res, i):
                res = i
                        
        for j in range(n):
            if (j != res and knows(res, j)) or not knows(j, res):
                return -1
        return res
                