## [Leetcode#700] Search in a Binary Search Tree
#
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None
        
        if root.val == val:
            return root
        
        left = self.searchBST(root.left, val)
        if left: return left
        
        right = self.searchBST(root.right, val)
        if right: return right
        
        return None