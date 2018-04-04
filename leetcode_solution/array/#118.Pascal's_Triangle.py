# [# 118] Pascal's Triangle
#  
#  twitter, apple
#
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        array = [[1], [1,1]]
        
        n = 2
        while n < numRows:
            subarray = [array[-1][i]+array[-1][i+1] for i in range(len(array[-1])-1)]
            array.append([1]+subarray+[1])
            n += 1
            
        return array