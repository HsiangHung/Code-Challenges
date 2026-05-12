## [Leetcode#119] Pascal's Triangle II
##
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ## Pascal's triangle:
        ## k
        ## 0      1
        ## 1     1 1
        ## 2    1 2 1
        ## 3   1 3 3 1  
        ## 4  1 4 6 4 1
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        array = [1,1]
        n = 2
        while n <= rowIndex:
            new_array =  []
            for i in range(len(array)-1):
                new_array.append(array[i]+array[i+1])
            new_array.append(1)
            new_array.insert(0,1)
            n += 1
            array[:] = new_array[:]
        return array