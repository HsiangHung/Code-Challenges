# [# 538] Convert BST to Greater Tree
#  
#  Amazon
#
#
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        
        self.sum = 0
        self.traversal(0, root)
        return root
        
        
    def traversal(self, sum, root):
        if not root.left and not root.right:
            root.val += self.sum
            self.sum = root.val
            return
        
        if root.right:
            self.traversal(sum, root.right)
        
        root.val += self.sum
        self.sum = root.val
        
        if root.left:
            self.traversal(sum, root.left)