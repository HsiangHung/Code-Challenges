# [#191] Number of 1 Bits
#
#  Microsoft, Apple
#
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #
        # idea: eg. 15= 8+7 = 8+4+3 = 8+4+2+1, 10=8+2
        #           search the binary number such that number >= n and store all binary numbers
        #       if n = 2**x, then number of bits = 1 
        #
        if n == 0: return 0
        
        bits = []
        
        factor = 1
        while factor < n:
            bits.append(factor)
            factor *= 2
            
        if factor == n: return 1
                
        count = 0
        while n >= 1 and len(bits) > 0:
            bit = bits.pop()
            if n >= bit:
                n -= bit
                count += 1
            
        return count