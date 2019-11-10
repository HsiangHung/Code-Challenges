## [Leetcode#67] Add Binary
##
## with a prepared binary array binary_sum = [0,0,..0] 
##
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = [int(s) for s in a][::-1]
        b = [int(s) for s in b][::-1]

        if len(a) >= len(b):
            short, long = b, a
        else:
            short, long = a, b
                    
        for i in range(len(short)):
            long[i] += short[i]
        
        for i in range(len(long)-1):
            if long[i] >= 2:
                long[i] -= 2
                long[i+1] += 1
        
        if long[-1] >= 2:
            long[-1] -= 2
            long.append(1)
                    
        return "".join([str(x) for x in long[::-1]])
                    