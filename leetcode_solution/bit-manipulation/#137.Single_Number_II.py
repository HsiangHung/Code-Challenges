#  137. Single Number II (medium)
#  https://leetcode.com/problems/single-number-ii/
#
class Solution:
    '''
    https://www.cnblogs.com/grandyang/p/4263927.html
    https://baihuqian.github.io/2018-06-23-single-number-ii/
    https://www.w3schools.com/python/python_operators.asp
    
     a b          a b            a b          a b
     0 0  + "1" = 0 1            0 0  + "0" = 0 0     b = b xor r & ~a;
     0 1  + "1" = 1 0            0 1  + "0" = 0 1     a = a xor r & ~b;
     1 0  + "1" = 0 0 (mod 3)    1 0  + "0" = 1 0       
     
     Number appearing once will survive on b. Number appearing three times won't. 
     
     extension:
     a b          a b            a b          a b
     0 0  + "1" = 0 1            0 0  + "0" = 0 0     b = b xor r;
     0 1  + "1" = 1 0            0 1  + "0" = 0 1     a = (a | r) & (~ r|(a ^ b))
     1 0  + "1" = 1 1            1 0  + "0" = 1 0
     1 1  + "1" = 0 0 (mod 4)    1 1  + "0" = 1 1   
     
    '''
    def singleNumber(self, nums: List[int]) -> int:
        
        a, b = 0, 0
        for num in nums:
            b = b^num & ~a
            a = a^num & ~b
            
        return b
            
            