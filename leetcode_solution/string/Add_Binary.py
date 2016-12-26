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
        n_a = len(a)
        n_b = len(b)
        
        if n_a > n_b:
            long_string = a
            short_string =b
        else:
            long_string = b
            short_string = a
            
        long_len = len(long_string)
        short_len = len(short_string)
            
        binary_sum = [0]*(long_len+1)
        for i in range(short_len):
            digit_a = int( long_string[ long_len-i-1])
            digit_b = int(short_string[short_len-i-1])
            binary_sum[long_len-i] +=  digit_a + digit_b
        
        for i in range(short_len, long_len):
            digit_a = int(long_string[long_len-i-1])
            binary_sum[long_len-i] += digit_a
        
        for i in range(long_len+1):
            print binary_sum[long_len-i]
            if binary_sum[long_len-i] == 3:
                binary_sum[long_len-i] = 1
                binary_sum[long_len-i-1] += 1
            elif binary_sum[long_len-i] == 2:
                binary_sum[long_len-i] = 0
                binary_sum[long_len-i-1] += 1
        
        if binary_sum[0] == 0: binary_sum.remove(0)

                
        return ''.join([str(x) for x in binary_sum])