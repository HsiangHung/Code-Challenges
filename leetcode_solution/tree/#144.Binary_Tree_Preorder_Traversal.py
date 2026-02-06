#  144. Binary Tree Preorder Traversal (easy)
#  https://leetcode.com/problems/binary-tree-preorder-traversal/
# 
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderIterative(self, root):
        """
        https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
        :type root: TreeNode
        :rtype: List[int]
        """        
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)