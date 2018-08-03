## [Leetcode#101] Symmetric Tree
## Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center). 
## For example, the binary tree ```[1,2,2,3,4,4,3]``` is symmetric, but ```[1,2,2,null,3,null,3]``` is not.
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.getSym(root.left, root.right)
        
    def getSym(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
            
        if left.val != right.val: return False
        
        return self.getSym(left.left, right.right) and self.getSym(left.right, right.left)
        