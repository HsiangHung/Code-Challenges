## [#190] Reverse Bits
#
#
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
       
        binary_digit = self.binarize(n)
        
        binary_digit += [0]*(32-len(binary_digit))
        
        factor = 1
        sum = 0
        for digit in binary_digit[::-1]:
            sum += digit*factor
            factor *= 2
            
        return sum
    
    def binarize(self, x):
        if x < 2: return [x % 2]
        return [x % 2] + self.binarize(x // 2)
        