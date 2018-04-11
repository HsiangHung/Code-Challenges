# [#230] Kth Smallest Element in a BST
#
#   google, Bloomber, Uber
#
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.nodes = []
        self.traversal(root, k)
        return self.nodes[k-1]
    
    def traversal(self, root, k):
        if not root.left and not root.right:
            self.nodes.append(root.val)
            return
        
        if root.left:
            self.traversal(root.left, k)
            
        self.nodes.append(root.val)
        if len(self.nodes) >= k: return
        
        if root.right:
            self.traversal(root.right, k)
            