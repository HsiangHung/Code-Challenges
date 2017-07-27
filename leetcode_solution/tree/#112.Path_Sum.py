## [Leetcode#112] Path Sum
## Given a binary tree and a sum, determine if the tree has a root-to-leaf path such 
## that adding up all the values along the path equals the given sum.

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False    
        return self.pathSum(sum, root, root.val)
    
    def pathSum(self, sum, root, pathsum):
        if not root.left and not root.right: 
            return sum == pathsum
        
        isSumExist = False
        if root.left:
            isSumExist = isSumExist or self.pathSum(sum, root.left, pathsum+root.left.val)
            
        if root.right:
            isSumExist = isSumExist or self.pathSum(sum, root.right, pathsum+root.right.val)
            
        return isSumExist