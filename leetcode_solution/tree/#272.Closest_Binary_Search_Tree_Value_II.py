#  272. Closest Binary Search Tree Value II (hard)
#  https://leetcode.com/problems/closest-binary-search-tree-value-ii/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.queue = []
        
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        '''
        data structure used is self.diff = [(diff1, sign1), (diff2, sign2),.....]
        self.diff is order by diff
        '''
        self.DFS(root, target, k)
        return [x[1] for x in self.queue[-k:]]
        
    def DFS(self, root, target, k):
        if not root: return
        if len(self.queue) >= k:
            if abs(root.val-target) >= self.queue[-1][0]:
                if root.val > target:
                    self.DFS(root.left, target, k)
                else:
                    self.DFS(root.right, target, k)
                return 
            elif abs(root.val-target) < self.queue[0][0]:
                self.queue.insert(0, (abs(root.val-target), root.val))
                self.queue.pop()
            else:
                self.insert(root, target, k)
        else:
            self.insert(root, target, k)
    
        self.DFS(root.left, target, k), self.DFS(root.right, target, k)
            
    def insert(self, root, target, k):
        i = 0
        while i <= len(self.queue)-1 and abs(root.val-target) >= self.queue[i][0]:
            i += 1
        self.queue.insert(i, (abs(root.val-target), root.val))
        self.queue = self.queue[:k]
        
        
        