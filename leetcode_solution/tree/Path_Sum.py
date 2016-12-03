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
        if root == None: return False
        
        path = self.getPath(root, sum, root.val, str(root.val))
        print path
        if path == None: return False
        return True
        
    def getPath(self, root, targetSum, sum, path):
        """
        : type root: TreeNode
        : type targetSum: int
        : type sum: int
        : type path: string
        : rtype: string
        """
        print root.val
        if not root.left and not root.right:
            if targetSum != sum: 
                return None
            else:
                return path
            
        if root.left:
            path_L = self.getPath(root.left, targetSum, sum+root.left.val, path+'->'+str(root.left.val))
            if path_L != None: return path_L
            
        if root.right:
            path_R = self.getPath(root.right, targetSum, sum+root.right.val, path+'->'+str(root.right.val))
            if path_R != None: return path_R