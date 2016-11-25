
# Depth-First-Search and Breadth-First-Search 


## Q1: [Leetcode#364] Nested List Weight Sum II
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

## Q2: [Leetcode#200] Number of Islands
### 
```Python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num =0 
        print grid
        y =0
        while y < len(grid):
            x = 0
            while x < len(grid[y]):
                if grid[y][x] == u'1':
                    num += 1
                    grid[y][x] = u'0'
                    self.DFS(grid,x,y)
                x += 1
            y += 1
        return num
        
    def DFS(self, grid, x, y):
        if x == len(grid[0]) or y == len(grid): return
        if x+1 < len(grid[0]) and grid[y][x+1] == u'1':
            grid[y][x+1] = u'0'
            self.DFS(grid,x+1,y)
            
        if x-1 >= 0 and grid[y][x-1] == u'1':
            grid[y][x-1] = u'0'
            self.DFS(grid,x-1,y)
            
        if y+1 < len(grid) and grid[y+1][x] == u'1':
            grid[y+1][x] = u'0'
            self.DFS(grid,x,y+1)
            
        if y-1 >= 0 and grid[y-1][x] == u'1':
            grid[y-1][x] = u'0'
            self.DFS(grid,x,y-1)
```

## Q3: [Leetcode#108] Convert Sorted Array to Binary Search Tree
### Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
```Python
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []: return None
        return self.root(nums)
        
    def root(self, nums):
        n = len(nums)
        if n == 1: return TreeNode(nums[0])
        
        half = nums[int(n/2)]
        node = TreeNode(half)
        node.left = self.root(nums[:int(n/2)])
        if  int(n/2)+1 < n:
            node.right = self.root(nums[int(n/2)+1:])
        return node
```
