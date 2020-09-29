# 766. Toeplitz Matrix
#
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(1, len(matrix)):
            if matrix[i][1:] != matrix[i-1][:-1]:
                return False
        
        return True
        