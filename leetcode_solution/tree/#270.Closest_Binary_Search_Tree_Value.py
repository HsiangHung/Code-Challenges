#  270. Closest Binary Search Tree Value (easy)
#  https://leetcode.com/problems/closest-binary-search-tree-value/
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def closestValue(self, root: TreeNode, target: float) -> int:
        '''
        need to go through entire tree. If use the criterion < min_diff to stop,
        then we will miss another closer node under the node.
        '''
        if not root.left and not root.right: return root.val
        
        output = root.val
        
        if root.left:
            val = self.closestValue(root.left, target)
            if abs(val-target) < abs(output-target): output = val                
        
        if root.right:
            val = self.closestValue(root.right, target)
            if abs(val-target) < abs(output-target): output = val  
                
        return output

#
#  The following is an optimal solution to search closest node.
#  Since it is a BST, we only search left if the current node root.val - target > 0
#  Similarly, only search right if root.val - target < 0
#
class OptSolution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        self.closest = root.val
        self.min_diff = root.val-target
        
        self.DFS(target, root)
        return self.closest
        
    def DFS(self, target, root):
        if not root: return
        
        diff = root.val-target
        
        if abs(diff) < abs(self.min_diff):
            self.closest = root.val
            self.min_diff = diff
            
        if self.min_diff == 0: return
        
        if root.left and root.right:
            if diff > 0: 
                self.DFS(target, root.left)
            elif diff < 0: 
                self.DFS(target, root.right)
        elif root.left:
            self.DFS(target, root.left)
        elif root.right:
            self.DFS(target, root.right)
        



