# [#476]  Number Complement
#
#
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ## no need to seriously convert to binary bits here.
        ## find the rules, and the problem is super easy
        ## eg num = 12, find the upper limit of 2**n =16,
        ## 
        ##              flip
        ##  8:  1000    0111 -> 7
        ##  9:  1001    0110 -> 6
        ## 10:  1010    0101 -> 5
        ## 11:  1011    0100 -> 4
        ## 12:  1100    0011 -> 3
        ## 13:  1101    0010 -> 2
        ## 14:  1110    0001 -> 1
        ## 15:  1111    0000 -> 0
        ## 16: 10000
        
        twoFactor = 2
        while twoFactor <= num:
            twoFactor *= 2
            
        return twoFactor-num-1
        