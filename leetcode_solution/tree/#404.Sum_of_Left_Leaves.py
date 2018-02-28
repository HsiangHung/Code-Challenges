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


    def sumLeftLeaves(self, root, branch):	
    
        sum = 0
        if not root.left and not root.right: 
            if branch == 'L': sum += root.val
            return sum

        if root.left:
            sum += self.sumLeftLeaves(root.left, 'L')
            
        if root.right:
            sum += self.sumLeftLeaves(root.right, 'R')
        
        return sum
        
        
## solution II:
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.traverse(root.left, root.right)
    
    def traverse(self, left, right):
        if not left and not right:
            return 0
        
        sum = 0
        if left:
            if not left.left and not left.right:
                sum += left.val
            else:
                sum += self.traverse(left.left, left.right)
            
        if right:
            sum += self.traverse(right.left, right.right)
            
        return sum