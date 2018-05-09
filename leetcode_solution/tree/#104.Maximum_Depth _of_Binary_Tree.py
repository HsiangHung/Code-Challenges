# [Leetcode#104] Maximum Depth of Binary Tree

#class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None        

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        max_depth = 1
        if root.left:
            max_depth = max(max_depth, self.maxDepth(root.left)+1)
            
        if root.right:
            max_depth = max(max_depth, self.maxDepth(root.right)+1)
        
        return max_depth      

