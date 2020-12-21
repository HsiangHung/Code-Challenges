#  156. Binary Tree Upside Down
#  https://leetcode.com/problems/binary-tree-upside-down/
#  
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        
        node = root
        while node.left != None:
            node = node.left

        self.DFS(root)                
        return node
        
    def DFS(self, root):
        if not root.left and not root.right: return
        
        left, right = root.left, root.right 
        
        if left: self.upsideDownBinaryTree(left) 
        if right: self.upsideDownBinaryTree(right) 
            
        left.left = right
        left.right = root
        root.left, root.right = None, None
            