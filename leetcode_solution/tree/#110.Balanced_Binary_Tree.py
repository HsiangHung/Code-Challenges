#  110. Balanced Binary Tree (easy)
#  https://leetcode.com/problems/balanced-binary-tree/ 
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
        return self.get_subtree_depth(root)

        
    def get_subtree_depth(self, root):
        if not root: return 0
        left_depth, right_depth = self.get_subtree_depth(root.left), self.get_subtree_depth(root.right)
        return False if (left_depth is False) or (right_depth is False) or (abs(left_depth - right_depth) > 1) else max(left_depth, right_depth) + 1
       
