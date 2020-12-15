#  1026. Maximum Difference Between Node and Ancestor (medium)
#  https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        '''
        Compare to solution 2, this solution is optimal in space.
        Only pass max_val and min_val in a root-leaf path with recursion way.
        '''
        if not root: return 0
        self.max_diff = 0
        self.DFS(root, root.val, root.val)
        return self.max_diff
    
    def DFS(self, root, max_val, min_val):        
        if not root.left and not root.right:
            self.max_diff = max(self.max_diff, max_val - min_val)
            return 
            
        if root.left:
            self.DFS(root.left, max(max_val, root.left.val), min(min_val, root.left.val))
            
        if root.right:
            self.DFS(root.right, max(max_val, root.right.val), min(min_val, root.right.val))
#
# 
class Solution2:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        '''
        this solution stores all ancestor nodes and look for all possible maximum.
        But it is not optimal in space
        '''
        self.max_diff = -float("inf")
        self.DFS(root, [])
        
        return self.max_diff

    
    def DFS(self, root, ancestors):
        
        if len(ancestors) > 0:
            for x in ancestors:
                self.max_diff = max(self.max_diff, abs(x-root.val))
   
        if not root.left and not root.right:
            return 
              
        if root.left:
            self.DFS(root.left, ancestors + [root.val])
            
        if root.right:
            self.DFS(root.right, ancestors + [root.val])
      