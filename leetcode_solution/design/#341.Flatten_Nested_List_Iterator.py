# #341. Flatten Nested List Iterator
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
        
        self.flat = []
        for x in nestedList:
            if x.isInteger():
                self.flat += [x.getInteger()]
            else:
                self.flat += self.flatten(x.getList())
        
        self.pointer = 0
                
    def next(self) -> int:
        val = self.flat[self.pointer]
        self.pointer += 1
        return val
                
    def flatten(self, nestList):
        output = []
        for x in nestList:
            if x.isInteger():
                output += [x.getInteger()]
            else:
                output += self.flatten(x.getList())
        return output
    
    def hasNext(self) -> bool:
        if self.pointer > len(self.flat)-1:
            return False
        else:
            return True
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())