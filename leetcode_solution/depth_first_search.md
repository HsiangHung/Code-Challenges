
# A. Depth-First-Search and Breadth-First-Search 


## Q1: Leetcode#364, Nested List Weight Sum II
### Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

```Python
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList == []: return 0
        self.depth = {}
        self.recursion(nestedList, 1)
        if self.depth == {}: return 0
        
        max_depth = max(self.depth.keys())
        sum_depth = 0
        for key in self.depth:
            sum_depth += (max_depth - key+1)*sum(self.depth[key])
            
        return sum_depth

    def recursion(self, nestedList, depth):
        for ch in nestedList:
            if ch.isInteger():
                if depth not in self.depth:
                    self.depth[depth] = [ch.getInteger()]
                else:
                    self.depth[depth].append(ch.getInteger())
            else: 
                self.recursion(ch.getList(), depth+1)
```

