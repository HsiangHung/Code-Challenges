# [#814] Binary Tree Pruning
#
#   Hulu
#
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        self.traversal(root)
        return root
    
    def traversal(self, root):
        if not root.left and not root.right:
            return root.val == 1
        
        subtreeHas1 = (root.val == 1)
        if root.left:
            leftHas1 = self.traversal(root.left)
            if not leftHas1: root.left = None
            subtreeHas1 = subtreeHas1 or leftHas1
            
        if root.right:
            rightHas1 = self.traversal(root.right)
            if not rightHas1: root.right = None
            subtreeHas1 = subtreeHas1 or rightHas1
            
        return subtreeHas1
        