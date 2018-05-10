## [Leetcode#202] Happy Number
##
## Uber, twitter, airbnb
##
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.recursion(n, set({}))
        
    def recursion(self, n, num_set):
        if n == 1: return True
        sum = 0
        for i in range(len(str(n))):
            sum += int(str(n)[i])**2
            
        if sum in num_set: return False
        num_set.add(sum)
        return self.recursion(sum, num_set)
        
        