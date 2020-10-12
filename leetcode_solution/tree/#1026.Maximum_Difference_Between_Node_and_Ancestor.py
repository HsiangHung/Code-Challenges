# #1026. Maximum Difference Between Node and Ancestor
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:       
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
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
      