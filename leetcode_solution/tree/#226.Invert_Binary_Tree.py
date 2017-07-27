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
        if not root: return root
        
        L = root.left
        R = root.right
        if L and R:
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif L and not R:
            self.invertTree(root.left)
        elif not L and R:
            self.invertTree(root.right)
        else:
            return root
        
        root.left = R
        root.right = L
        
        return root