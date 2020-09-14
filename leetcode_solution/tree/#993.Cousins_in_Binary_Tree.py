# # 993. Cousins in Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        if not root: return False
        
        self.cousins = {}
        self.DFS(root, x, y, [None,])
        
        return (self.cousins[x][0] == self.cousins[y][0]) and (self.cousins[x][1] != self.cousins[y][1])
        
        
    def DFS(self, root, x, y, path):
        
        if root.val == x or root.val == y:
            self.cousins[root.val] = (len(path), path[-1])
        
        if not root.left and not root.right:
            return
                
        if root.left:
            self.DFS(root.left, x, y, path+[root.val])
            
        if root.right:
            self.DFS(root.right, x, y, path+[root.val])
        