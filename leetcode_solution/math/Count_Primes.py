## [Leetcode#204] Count Primes
##
## create an array [1,1,1.....1] with size of n
## and turn to 0 if 2,3,4....; 3,6,9.....; 5,10,15....
## the number of remaining '1' = number of prime numbers
##
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n <=2: return 0
        
        primes = [1]*n
        primes[0] = 0
        primes[1] = 0
        
        i = 2
        while i <= int(math.sqrt(n)):
            j = 2*i
            while j < n:
                if primes[j] == 1: primes[j] = 0
                j += i
            i +=1
        return sum(primes)