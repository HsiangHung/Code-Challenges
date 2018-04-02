# [# 357] Count Numbers with Unique Digits
#  
#   Google
#
#
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 10
        
        #return self.dynamicalProgrammingCount(n)
        
        ## the following analyzes number of possible combinations to solve:
        # the number of unique numbers (not repeated) is given by 
        # if n=2, 10*9 + 1 ('0')
        # if n=3, 10*9*8, if there are 2 zeros, we have 001, 010 (but not 100) so 10*9*8+9*2
        # if n=4, 10*9*8*7, 3 zeros: 0001, 0010 but not 0100: 9*2
        #                   2 zeros: 0036, 0360, 0306, so 9*8*3                so 10*9*8*7+9*2+9*8*3
        # if n=5, 10*9*8*7*6, 4 zeros, 00001, 00010: 9*2
        #                     3 zeros, 00130, 00103, 00013: 9*8*3
        #                     2 zeros, 01230, 01203, 01023, 00123: 9*8*7*4     so 10*9*..*6 + 9*2+9*8*3+9*8*7*4
        
        num_ways = self.multiplication(range(10, 10-n, -1))

        num_zeros = 2
        while num_zeros < n:
            num_ways += self.multiplication(range(9, 9-(num_zeros-1), -1))*num_zeros
            num_zeros += 1

        return num_ways + 1
        
    def multiplication(self, nums):
        val = 1
        for num in nums:
            val *= num
        return val


    def dynamicalProgrammingCount(self, n):
        '''this method uses dynamical programming, but cannot pass when n >= 6 
           for time limit exceeded
        '''
        dp = {2: set({11,22,33,44,55,66,77,88,99})}
        num_digit = 3
        while num_digit <= n:
            
            dp[num_digit] = set({})
            repeat_num = [str(x) for x in dp[num_digit-1]]
            
            for num in repeat_num:
                for digit in [str(x) for x in range(10)]:
                    
                    dp[num_digit].add(int(digit+num))
                    for i in range(1, len(num)+1):
                        dp[num_digit].add(int(num[:i]+digit+num[i:]))
                   
            for digit in [str(x) for x in range(1, 10)]:
                dp[num_digit].add(int(digit+''.join(['0']*(num_digit-1))))
            
            num_digit +=1 
            
        return 10**n-len(dp[n])