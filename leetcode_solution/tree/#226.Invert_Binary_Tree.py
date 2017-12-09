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
        if not root.left and not root.right: return root
        
        if root.left and root.right:
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root.left:
            self.invertTree(root.left)
        else:
            self.invertTree(root.right)
            
        root.left, root.right = root.right, root.left
        
        return root