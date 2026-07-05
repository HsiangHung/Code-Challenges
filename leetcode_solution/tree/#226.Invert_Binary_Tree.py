## [Leetcode#226] Invert Binary Tree
## 
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 

        l, r = self.invertTree(root.left), self.invertTree(root.right)
        root.left, root.right = r, l
        
        return root