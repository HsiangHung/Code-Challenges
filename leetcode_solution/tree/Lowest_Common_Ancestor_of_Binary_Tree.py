## [Leetcode#236] Lowest Common Ancestor of a Binary Tree
##
## here I store the path along q and along q as two lists in self.acnestor.
##  but the code passed 29/31, with memory access limit.
##
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
 
        self.path = []
        self.traverse(root, p)
        path_p = self.path

        self.path = []
        self.traverse(root, q)
        path_q = self.path

        if len(path_p) <= len(path_q):
            path_q = set(path_q)
            for node in path_p:
                if node in path_q: return node
        else:
            path_p = set(path_p)
            for node in path_q:
                if node in path_p: return node
        
        
    def traverse(self, root, p):
        if root == p: 
            self.path = [root]
            return
        
        if not root.left and not root.right: return
        if root.left != None: 
            self.traverse(root.left, p)
            if len(self.path) !=0: 
                self.path.append(root)
                return 
        
        if root.right != None: 
            self.traverse(root.right, p)
            if len(self.path) !=0: 
                self.path.append(root)
                return