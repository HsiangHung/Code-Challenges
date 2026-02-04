## [Leetcode#111] Minimum Depth of Binary Tree
##
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        if root.left and root.right:
            return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1)
        elif root.left and not root.right:
            return self.minDepth(root.left)+1
        elif not root.left and root.right:
            return self.minDepth(root.right)+1
        else: # if root has no children
            return 1