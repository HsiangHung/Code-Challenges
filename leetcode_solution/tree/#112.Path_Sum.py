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
        return sum in set(self.pathSum(root))
        
    def PathSum(self, root):
        if not root.left and not root.right: return [root.val]
        
        path_sum = []
        if root.left:
            path_sum += [root.val+x for x in self.pathSum(root.left)]
            
        if root.right:
            path_sum += [root.val+x for x in self.pathSum(root.right)]
        
        return path_sum


## solution-2

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        return self.traversal(root, sum, root.val)
    
    def traversal(self, root, sum, pathsum):
        if not root.left and not root.right:
            if pathsum == sum: return True
            return False
        
        hasPathSum = False
        if root.left:
            hasPathSum = hasPathSum or self.traversal(root.left, sum, pathsum+root.left.val)
            
        if root.right:
            hasPathSum = hasPathSum or self.traversal(root.right, sum, pathsum+root.right.val)
            
        return hasPathSum
        
