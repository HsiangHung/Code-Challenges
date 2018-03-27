# [#204] Count Primes
#
#
#
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy as np
        if n <= 2: return 0
        
        # prepare a list [0,0,1,1,1,.....1]
        # if a number has been scned, then turn the index = 0
    
        nums = [1]*n
        nums[0], nums[1] = 0, 0

        num_prime_num = 0
        
        prime_num = 2
        while prime_num < n:
            
            if nums[prime_num] == 1:
                num_prime_num += 1
                
                num = 2*prime_num
                while num < n:
                    nums[num] = 0
                    num += prime_num
                    
            prime_num += 1
            
        return num_prime_num