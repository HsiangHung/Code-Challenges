#  341. Flatten Nested List Iterator (medium)
#  https://leetcode.com/problems/flatten-nested-list-iterator/
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        '''
        We need to prepare the flat nest first but calls next() and hasNext().
        Otherwsie while i.appen(next()), there are still [[1,5], [2,3,4], ...] structures
        So the self.pointer is the pointer on the flatten array.
        '''
        self.data = self.DFS(nestedList)
        self.pointer = 0
    
    def next(self) -> int:
        x = self.data[self.pointer]
        self.pointer += 1
        return x
        
    def hasNext(self) -> bool:
        return self.pointer < len(self.data)
    
    def DFS(self, nest):
        ans = []
        for x in nest:
            if x.isInteger():
                ans += [x.getInteger()]
            else:
                ans += self.DFS(x.getList())
        return ans
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())