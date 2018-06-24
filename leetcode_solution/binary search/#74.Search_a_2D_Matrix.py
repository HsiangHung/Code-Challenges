## [#74] Search a 2D Matrix
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
        
        #
        # idea: run lower bound binary search for x and y
        #
        
        vertical = [x[0] for x in matrix]
        y = self.BS_lowerBound(vertical, target)
        
        if matrix[y][0] == target: return True
        
        horizontal = matrix[y]
        x = self.BS_lowerBound(horizontal, target)
        
        if x >= 0 and matrix[y][x] == target: return True
        return False
        
        
    def BS_lowerBound(self, vertical, target):
        '''lower bound binary search algorithm'''
        if len(vertical) == 1:
            if vertical[0] <= target: return 0
            return -1
 
        if len(vertical) == 2:
            if vertical[0] <= target < vertical[1]: return 0
            if vertical[1] <= target: return 1
            return -1
                
        mid = len(vertical) // 2
        if vertical[mid] == target:
            return mid
        elif vertical[mid] > target:
            return self.BS_lowerBound(vertical[:mid], target)
        elif vertical[mid] < target:
            return mid+1+self.BS_lowerBound(vertical[mid+1:], target)
          