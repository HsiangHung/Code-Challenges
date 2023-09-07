#  1038. Binary Search Tree to Greater Sum Tree (medium)
#  https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
#  Ebay
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        self.sum = 0

        def DFS(root):
            if not root: return
            if root.right:
                DFS(root.right)

            val = root.val
            root.val = self.sum + val
            self.sum += val

            if root.left:
                DFS(root.left)

        DFS(root)
        return root