#  235. Lowest Common Ancestor of a Binary Search Tree (easy)
#  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#  
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) 
# of two given nodes in the BST.

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
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


