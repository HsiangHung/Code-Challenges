#  285. Inorder Successor in BST (medium)
#  https://leetcode.com/problems/inorder-successor-in-bst/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.successor = None
        self.search = True
        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return None
        
        self.inorderSuccessor(root.left, p)
        
        if not self.search:  # note, this one needs to be prior to self.search = False sentence
            if not self.successor: self.successor = root
        
        if root == p: self.search = False
        
        self.inorderSuccessor(root.right, p)
        
        return self.successor
            