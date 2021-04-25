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
        self.ans = 1
        self.DFS(root.left, root.val)
        self.DFS(root.right, root.val)
        return self.ans
    
    def DFS(self, root, max_val):
        if not root: return
        
        if root.val >= max_val: 
            self.ans += 1
            max_val = max(max_val, root.val)
        
        self.DFS(root.left, max_val) 
        self.DFS(root.right, max_val)