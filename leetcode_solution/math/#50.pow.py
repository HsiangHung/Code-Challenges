#[# 50] Pow(x, n)
#
class Solution(object):
    '''
    this solution is first to convert an integer to a binary number
    and then decompose it. e.g. 10 = 1010, so x^10 = .....
    see http://bangbingsyb.blogspot.com/2014/11/leetcode-powx-n.html
    '''
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



class Solution2:
    def myPow(self, x: float, n: int) -> float:
        '''
        using recursion, myPower(x, 10) = myPower(x, 5)^2*x = (myPower(x, 2)^2*x)^2*x ... until power=1
        https://zxi.mytechroad.com/blog/math/leetcode-50-powx-n/
        '''
                
        factor = 1 if n % 2 == 1 else 0
        
        if n > 0:
            if n == 1: return x
        elif n < 0:
            if n == -1: return 1/x
        else:
            return 1
        
        power = self.myPow(x, n // 2)
        return power*power*(x**factor)