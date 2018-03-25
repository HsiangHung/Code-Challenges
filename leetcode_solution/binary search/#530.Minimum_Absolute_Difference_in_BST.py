# [#530] Minimum Absolute Difference in BST
#
#
#
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.prevRoot = None
        self.inorder_traversal(root)
        return self.minAbs
        
        
    def inorder_traversal(self, root):
        if not root.left and not root.right:
            self.helper(root)
            return
        
        if root.left:
            self.inorder_traversal(root.left)
        
        self.helper(root)
        
        if root.right:
            self.inorder_traversal(root.right)
            
            
    def helper(self, root):
        if self.prevRoot is None:
            self.minAbs = float('inf')
        else:
            self.minAbs = min(self.minAbs, abs(root.val-self.prevRoot.val))
        self.prevRoot = root
        