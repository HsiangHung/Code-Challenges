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
        self.flatten = []
        for x in nestedList:
            if x.isInteger():
                self.flatten.append(x.getInteger())
            else:
                self.flatten += self.DFS(x.getList())
        self.pointer = 0
            
    def next(self) -> int:
        if self.hasNext():
            x = self.flatten[self.pointer]
            self.pointer += 1
            return x
       
    def DFS(self, nest):
        ans = []
        for x in nest:
            if x.isInteger():
                ans.append(x.getInteger())
            else:
                ans += self.DFS(x.getList())
        return ans
                    
    def hasNext(self) -> bool:
        return len(self.flatten) > self.pointer
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())