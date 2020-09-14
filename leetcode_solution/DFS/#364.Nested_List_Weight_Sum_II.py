# #364. Nested List Weight Sum II
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def __init__(self):
        self.sum = 0
        
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        '''
        a toy example: nestedList = [[2], 3, [[1]]]
        trick: deep first search the maximum depth first.
        deeper, smaller depth, so use max_depth-current_depth
        '''
        self.max_depth = self.get_max_depth(nestedList)
        
        _ = self.DFS(nestedList, 0)
        return self.sum
        
    def DFS(self, nestedList, depth):

        integers = []
        
        for x in nestedList:
            if not x.isInteger():
                self.DFS(x.getList(), depth+1)
            else:
                integers.append(x.getInteger())
            
        for x in integers:
            self.sum += (self.max_depth-depth)*x
        
        return depth + 1
        
    def get_max_depth(self, nestedList):    
        depth = 0
        for x in nestedList:
            if not x.isInteger():
                depth = max(depth, self.get_max_depth(x.getList()))
        return depth + 1        