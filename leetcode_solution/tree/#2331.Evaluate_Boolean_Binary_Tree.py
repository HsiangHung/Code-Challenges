#
# 2331. Evaluate Boolean Binary Tree
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right:
            return True if root.val == 1 else False

        left, right = self.evaluateTree(root.left), self.evaluateTree(root.right)

        if root.val == 2: # "OR"
            return left or right
        else: # "AND"
            return left and right