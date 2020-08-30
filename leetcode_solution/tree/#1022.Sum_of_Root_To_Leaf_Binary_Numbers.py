#1022. Sum of Root To Leaf Binary Numbers
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root: return 0
                
        self.path_sum = 0
        self.DFS(root, 0)
        return self.path_sum
        
    
    def DFS(self, root, path_sum):
        
        path_sum += root.val
        
        if not root.left and not root.right: 
            self.path_sum += path_sum
            return
    
        if root.left:
            self.DFS(root.left, 2*path_sum)
            
        if root.right:
            self.DFS(root.right, 2*path_sum)
    
    
    