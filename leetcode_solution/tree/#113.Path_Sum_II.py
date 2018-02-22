## [Leetcode#113] Path Sum II
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        self.paths = []
        self.helper(root, [], sum)
        return self.paths
    
    def helper(self, root, path, sum):
        import numpy as np
        if not root.left and not root.right:
            if np.sum(path) + root.val == sum:
                self.paths.append(path + [root.val])
                
            return
          
        if root.left:
            self.helper(root.left, path+[root.val], sum)
            
        if root.right:
            self.helper(root.right, path+[root.val], sum)
            
        
        