# 1428. Leftmost Column with at Least a One
#
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()

        x, y = col-1, 0
        while x >= 0 and y < row:
            elem = binaryMatrix.get(y, x)
            if elem == 0:
                y += 1
            else:
                x -= 1
        
        return x+1 if x != col-1 else -1