# [# 69] Sqrt(x)
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return x
        
        upper = x/2 + 1
        lower = 1
        
        while upper-lower > 1:
            middle = int((upper+lower)/2)
            #print lower, middle, upper
            if x > middle**2:
                lower = middle
            elif x < middle**2:
                upper = middle
            elif x == middle**2:
                return middle
        
        return lower
    
    def mySqrt_float(self, x):
        '''
        this method is useful for if we need to retun a more accurate float number
        type x: int
        rtype: float
        '''
        if x <= 1: return x

        i = 1
        while i**2 < x:
            i += 1
       
        x1 = i-1
        x2 = float(x)/x1
        avg = (x1+x2)/2
        while abs(avg**2 - x) >= 0.01:
            x1 = x/avg
            x2 = avg
            avg = (x1+x2)/2
            
        return  avg