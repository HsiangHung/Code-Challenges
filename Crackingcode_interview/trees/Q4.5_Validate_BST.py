## [Leetcode#98] Validate Binary Search Tree
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        self.stack = -float('inf')
        self.isBST = True
        
        self.BST(root)
        return self.isBST
        
        
    def BST(self, root):
        if root.left == None and root.right == None:
            if root.val <= self.stack: 
                self.isBST = False
            else:
                self.stack = root.val
            return
        
        if root.left != None: self.BST(root.left)
        
        if root.val <= self.stack: 
            self.isBST = False
            return
        else:
            self.stack = root.val
                
        if root.right != None: self.BST(root.right)
        