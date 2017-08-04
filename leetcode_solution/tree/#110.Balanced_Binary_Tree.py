## [Leetcode#110] Balanced Binary Tree
## Given a binary tree, determine if it is height-balanced.
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
		if not root: return True
        
        if self.traverse(root) < 0: return False
        return True
        
    def traverse(self, root):
        if not root.left and not root.right: return 0
        
        L_depth, R_depth = 0, 0
        if root.left:
            L_depth += self.traverse(root.left) + 1
        
        if root.right:
            R_depth += self.traverse(root.right) + 1
        
        if min(L_depth, R_depth) < 0 or abs(L_depth-R_depth) > 1: return -2
                
        return max(L_depth, R_depth)