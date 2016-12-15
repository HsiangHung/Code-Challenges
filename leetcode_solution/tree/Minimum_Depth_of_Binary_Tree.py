## [Leetcode#111] Minimum Depth of Binary Tree
##
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.getDepth(root)
        
        
    def getDepth(self, root):
        if root.left == None and root.right == None: return 1
        
        if root.left != None and root.right != None: 
            return min(self.getDepth(root.left), self.getDepth(root.right))+1
        elif root.left != None and root.right == None:
            return self.getDepth(root.left)+1
        elif root.left == None and root.right != None:
            return self.getDepth(root.right)+1