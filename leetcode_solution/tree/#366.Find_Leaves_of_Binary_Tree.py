#  366. Find Leaves of Binary Tree (medium)
#  https://leetcode.com/problems/find-leaves-of-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.leaves = []
        if not root: return self.leaves
        self.DFS(root)
        return self.leaves
    
    def DFS(self, root):
        if not root.left and not root.right:
            reverse_depth = 1
            self.insert_leaves(root, reverse_depth)
            return reverse_depth
        
        if root.left and root.right:
            reverse_depth = max(self.DFS(root.left), self.DFS(root.right)) + 1
        elif root.left:
            reverse_depth = self.DFS(root.left) + 1
        elif root.right:
            reverse_depth = self.DFS(root.right) + 1
        
        self.insert_leaves(root, reverse_depth)            
        return reverse_depth

    def insert_leaves(self, root, depth):
        if len(self.leaves) < depth:
            self.leaves.append([root.val])
        else:
            self.leaves[depth-1].append(root.val)
            