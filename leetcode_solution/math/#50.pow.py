#[# 50] Pow(x, n)
#
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        binary_num = self.binarize(abs(n))
        
        #print binary_num
        
        if n >0:
            factor = x
        else:
            factor = 1/x
            
        product = 1
        for num in binary_num:
            if num == 1: product *= factor
            #print factor
            factor = factor**2
            
        return product
        
        
    def binarize(self, x):
        bin = []
        while x >= 1:
            bin.append(x % 2)
            x = x // 2
            
        return bin