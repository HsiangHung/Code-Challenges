## [Leetcode#235]Lowest Common Ancestor of a Binary Search Tree
## Given a binary search tree (BST), find the lowest common ancestor (LCA) 
## of two given nodes in the BST.

#class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
         

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None: return None
        if p.val > q.val:
            return self.getNode(root, q, p)
        else:
            return self.getNode(root, p, q)
        
    def getNode(self, root, p, q):
        """
        : type root, p, q: TreeNode (q > p)
        : rtype: int
        """
        if p.val <= root.val <= q.val: return root.val
        
        if p.val <= root.val and q.val <= root.val:
            return self.getNode(root.left, p, q)
            
        if p.val >= root.val and q.val >= root.val:
            return self.getNode(root.right, p, q)



