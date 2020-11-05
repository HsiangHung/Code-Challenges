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
        if not root: return
        self.element = []
        self.DFS(root, k)
        print (self.element)
        return self.element[k-1]
        
    def DFS(self, root, k):
        if len(self.element) >= k: return 
        if root.left: self.DFS(root.left, k)
        self.element.append(root.val)
        if root.right: self.DFS(root.right, k)
            