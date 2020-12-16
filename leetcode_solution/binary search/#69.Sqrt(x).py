#  69. Sqrt(x) (easy)
#  https://leetcode.com/problems/sqrtx/
#
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Bisection method
        https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%B3%95_(%E6%95%B8%E5%AD%B8)
        '''
        def f(y):
            return y*y-x
        
        if x <= 1: return x
        
        y1, y2, mid = 0, x, x / 2
        while int(y1) != int(y2):
            if f(mid) == 0: return int(mid)
            
            if f(mid)*f(y2) < 0:
                y1 = mid
                mid = (y1+y2)/2
            else:
                y2 = mid
                mid = (y1+y2)/2
        
        return int(mid)
