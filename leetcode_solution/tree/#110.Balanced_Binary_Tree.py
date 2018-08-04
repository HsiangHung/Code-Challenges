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
        if not root: return True
        return self.get_subtree_depth(root) != - 1

        
    def get_subtree_depth(self, root):
        if not root: return 0
        
        left_depth, right_depth = self.get_subtree_depth(root.left), self.get_subtree_depth(root.right)
        
        if left_depth == -1 or right_depth == -1 or abs(left_depth-right_depth) > 1:
            return -1
        else:
            return max(left_depth + 1, right_depth + 1)

