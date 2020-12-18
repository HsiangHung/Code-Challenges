#  1004. Max Consecutive Ones III (medium)
#  https://leetcode.com/problems/max-consecutive-ones-iii/
#
class Solution:
    '''
    https://blog.csdn.net/fuxuemingzhu/article/details/88093268
    
    A = [1,1,1,0,0,0,1,1,1,1,0]  K= 2
         0 1 2 3 4 5 6 7 8 9 10
    
         i  j  A[i]  A[j]  zeros  max_zeros
         0  0    1     1     0     1
         0  1    1     1     0     2
         0. 2.   1.    1.    0.    3
         0. 3.   1.    0.    1.    4
         0. 4.   1     0.    2.    5
         0. 5.   1.    0.    3.   
         
     =>  run i until zeros < K if A[i] == 0
     
         4. 6.   0.    1.    2     5
         4. 7.   0.    1.    2.    5
         4. 8.   0.    1.    2     5
         4. 9.   0.    1.    2.    5
         4 10.   0     0.    2.    6
    '''
    def longestOnes(self, A: List[int], K: int) -> int:
        
        max_sub = 0
        i, zeros = 0, 0
        for j in range(len(A)):
            print (i, j, A[i], A[j], zeros, max_sub)
            if A[j] == 0:
                zeros += 1
            
            while zeros > K:
                if A[i] == 0:
                    zeros -= 1
                i += 1
        
            max_sub = max(max_sub, j - i + 1)
        
        return max_sub
        