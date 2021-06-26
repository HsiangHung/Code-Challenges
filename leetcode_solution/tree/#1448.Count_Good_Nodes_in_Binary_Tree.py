#  1448. Count Good Nodes in Binary Tree (medium)
#  https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        return self.traversal(root, root.val)
        
    def traversal(self, root, max_val):
        if not root: return 0
        
        L = self.traversal(root.left, max(max_val, root.val)) 
        R = self.traversal(root.right, max(max_val, root.val))
        
        if max_val <= root.val:
            return L + R + 1
        else:
            return L + R