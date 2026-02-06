#  94. Binary Tree Inorder Traversal (medium)
#  https://leetcode.com/problems/binary-tree-inorder-traversal/
#
#  iteration for inorder tree traversal
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root: 
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) 