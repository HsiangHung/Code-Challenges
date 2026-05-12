## [Leetcode#396] Rotate Function
##
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # F(0) =   0*A[0]+1*A[1]  +2*A[2]+..+(n-2)*A[n-2]+(n-1)*A[n-1]
        # F(1) = 0*A[n-1]+1*A[0]  +2*A[1]+..+(n-2)*A[n-3]+(n-1)*A[n-2]
        # F(2) = 0*A[n-2]+1*A[n-1]+2*A[0]+..+(n-2)*A[n-4]+(n-1)*A[n-3]
        # ....
        # F(n-2) = 0*A[2]+1*A[3]  +2*A[4]+..+(n-2)*A[0]  +(n-1)*A[1]
        # F(n-1) = 0*A[1]+1*A[2]  +2*A[3]+..+(n-2)*A[n-1]+(n-1)*A[0]
        #
        # F(1)-F(0) = 0*A[n-1]+A[0]+A[1]+A[2]+..+A[n-2] -(n-1)*A[n-1] = sum - n*A[n-1]
        # F(2)-F(1) = 0*A[n-2]+A[0]+A[1]+...    +A[n-3] -(n-1)*A[n-2] = sum - n*A[n-2]
        # ...
        # F(n-1)-F(n-2) = 0*A[1]+A[2]+A[3]+..+A[n-1]+A[0] - (n-1)A[1] = sum - n*A[1]
        
        sum_A = sum(A)
        F0 = 0
        for i in range(len(A)):
            F0 += i*A[i]
            
        max_val = F0
        for i in range(len(A)-1):
            new_F = F0 + sum_A - len(A)*A[len(A)-1-i]
            max_val = max(max_val, new_F)
            F0 = new_F
            
        return max_val
            