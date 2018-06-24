## [#240] Search a 2D Matrix II
#
#
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]: return False
        
        x, y = 0, len(matrix)-1
        while x < len(matrix[0]) and y >= 0:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                x += 1
            elif matrix[y][x] > target:
                y -= 1
                
        return False