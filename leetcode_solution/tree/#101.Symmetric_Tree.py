#  101. Symmetric Tree (easy)
#  https://leetcode.com/problems/symmetric-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.DFS(root.left, root.right)
        
    def DFS(self, left, right):
        if left and right:
            if left.val != right.val:
                return False
            else:
                return self.DFS(left.left, right.right) and self.DFS(left.right, right.left)
        elif not left and not right:
            return True
        else:
            return False