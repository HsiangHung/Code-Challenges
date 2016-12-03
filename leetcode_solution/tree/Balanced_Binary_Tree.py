## [Leetcode#110] Balanced Binary Tree
## Given a binary tree, determine if it is height-balanced.
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
		if root == None: return True
		
		h = self.getHeight(root)+1
        if h == -1: return False
        return True


    def getHeight(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        if root.left == None and root.right == None: return 0

		h_L, h_R = 0, 0 
        if root.left != None:
            h_L = self.getHeight(root.left)+1

        if root.right != None:
            h_R = self.getHeight(root.right)+1
        
        if h_L == -1 or h_R == -1: return -2
            
        diff = abs(h_L-h_R)
        if diff <= 1: 
            return max(h_L, h_R)
        else:
            return -2
