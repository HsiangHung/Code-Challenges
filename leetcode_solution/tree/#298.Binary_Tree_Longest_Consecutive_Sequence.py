#  298. Binary Tree Longest Consecutive Sequence (medium)
#  https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0
        self.longest = 1
        self.DFS(root, 1)
        return self.longest
    
    def DFS(self, root, length):
        
        self.longest = max(self.longest, length)
        
        if not root.left and not root.right: return
        
        if root.left:
            if root.left.val == root.val + 1:
                self.DFS(root.left, length +1)
            else:
                self.DFS(root.left, 1)
                
        if root.right:
            if root.right.val == root.val + 1:
                self.DFS(root.right, length +1)
            else:
                self.DFS(root.right, 1)