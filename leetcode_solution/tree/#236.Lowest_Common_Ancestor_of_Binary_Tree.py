#  236. Lowest Common Ancestor of a Binary Tree (medium)
#  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    * if both childs give true, the root must be the common acnestor
    * if one child gives true, and root is either p or q, then the root must be common acnestor
    * otherwise still return true if child has p or q
    * note once the common ancestor is found, we should stop search.
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        self.ancestor = None
        self.DFS(root, p, q)
        return self.ancestor
    
    def DFS(self, root, p, q):
        if not root: return False
        
        if self.ancestor: return  # once found common acnestor, stop search
        
        l, r = self.DFS(root.left, p, q), self.DFS(root.right, p, q)

        if root.val in (p.val, q.val):
            if l or r:
                self.ancestor = root
            return True
        else:
            if l and r:
                self.ancestor = root
                return True
            else:
                return l or r
            
            
            