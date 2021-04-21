#  240. Search a 2D Matrix II (medium)
#  https://leetcode.com/problems/search-a-2d-matrix-ii/
#
class Solution:
    '''
    somehow, using BFS in this problem cannot pass all test cases in Leetcode

    https://www.cnblogs.com/grandyang/p/4669134.html
    using DFS, start from lower left corner, and search up-right.
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.found = False
        self.DFS(0, len(matrix)-1, matrix, target)
        return self.found
        
        
    def DFS(self, x, y, matrix, target):
        if self.found: return 
        
        if matrix[y][x] == target:
            self.found = True
        elif matrix[y][x] > target:
            if y > 0: 
                self.DFS(x, y-1, matrix, target)
        else:
            if x < len(matrix[0]) -1:
                self.DFS(x+1, y, matrix, target)