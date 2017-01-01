## Q1.7 set entire row and column to zero if there is a zero element.
## this is the same as Leetcode#73.
## 
## here I used space complexity O(M+N)
##
def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix[0])
    n = len(matrix)
        
    zeroRow = set({})
    zeroCol = set({})
        
    for y in range(n):
    	for x in range(m):
            if matrix[y][x] == 0:
                zeroRow.add(y)
                zeroCol.add(x)
                    
    for y in zeroRow:
        for x in range(m):
            matrix[y][x] = 0
                
    for x in zeroCol:
        for y in range(n):
            matrix[y][x] =0