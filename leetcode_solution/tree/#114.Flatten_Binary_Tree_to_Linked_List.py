## [#114] Flatten Binary Tree to Linked List
#
#  Microsoft
#
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.last_node = None
        self.traversal(root)
        
    def traversal(self, root):
        if not root.left and not root.right:
            self.last_node = root
            return
        
        if root.left:
            self.flatten(root.left)
            
        if root.right:
            right = root.right
            if self.last_node:
                self.last_node.right = right
                self.last_node.left = None
            self.flatten(right)
            
        if root.left:
            root.right = root.left
            root.left = None
                