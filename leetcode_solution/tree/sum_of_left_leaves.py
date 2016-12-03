## [Leetcode#404] Sum of Left Leave
## Find the sum of all left leaves in a given binary tree.   
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        return self.sumLeftLeaves(root, 'N')

    def sumLeftLeaves(self, root, D):
        if not root.left and not root.right: 
            if D == 'L': return root.val
            return 0
            
        sum =0
        
        if root.left != None:
            sum += self.sumLeftLeaves(root.left, 'L')
            
        if root.right != None:
            sum += self.sumLeftLeaves(root.right, 'R')
        
        return sum