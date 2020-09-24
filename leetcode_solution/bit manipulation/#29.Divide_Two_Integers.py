# # 29. Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        NOTE, int range is -2147483648 <= x <= 2147483647.
        as long as outside the range, positive x = 2147483647, negative x = -2147483648
        '''
        self.divisor = divisor 
        
        if abs(dividend) < abs(divisor): return 0
                
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return min(self.DFS(abs(dividend), abs(divisor), 1), 2147483647) 
        else:
            return max(-self.DFS(abs(dividend), abs(divisor), 1), -2147483648)
       
        
    def DFS(self, dividend, divisor, quote):
        
        if dividend <= divisor: 
            # here is to fine remainder. Still use recursion and double divisor and quote
            if dividend < abs(self.divisor):
                return 0
            else:
                divisor = abs(self.divisor)
                quote = 1
                return self.DFS(dividend-divisor, divisor+divisor, quote+quote) + quote
        
        return self.DFS(dividend-divisor, divisor+divisor, quote+quote) + quote
   