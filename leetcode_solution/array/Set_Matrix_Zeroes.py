## [Leetcode#73] Set Matrix Zeroes
##
##  Here I use space complexity O(1) and time complexity O(MN)
##
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0])
        n = len(matrix)
        
        ## check if there are zeros in the first row; if yes, future we need to 
        ## set all elements in this row to zeros
        firstRow_zeros = False
        for x in range(m):
            if matrix[0][x] == 0: 
                firstRow_zeros = True
                break
                
        ## check if there are zeros in the first col; if yes, future we need to 
        ## set all elements in this row to zeros
        firstCol_zeros = False    
        for y in range(n):
            if matrix[y][0] == 0: 
                firstCol_zeros = True
                break
        
        ## if M(i,j) =0, then set M(i,0) = M(j,0) =0.
        for y in range(1,n):
            for x in range(1,m):
                if matrix[y][x] == 0: 
                    matrix[0][x] = 0
                    matrix[y][0] = 0
                    
        for x in range(1,m):
            if matrix[0][x] == 0:
                for y in range(1, n):
                    matrix[y][x] = 0
                    
        for y in range(1,n):
            if matrix[y][0] == 0:
                for x in range(1, m):
                    matrix[y][x] = 0
         
        ## now it is time set first row to zeros if there are zeros in first row           
        if firstRow_zeros:
            for x in range(m):
                matrix[0][x] = 0
        
        ## now it is time set first col to zeros if there are zeros in first col        
        if firstCol_zeros:
            for y in range(n):
                matrix[y][0] = 0
                    