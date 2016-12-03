## [Leetcode#199] Binary Tree Right Side View
##
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        
        self.views= []
        self.traverse(root, 1)
        return self.views
        
        
    def traverse(self, root, depth):
        if len(self.views) < depth: self.views.append(root.val)
        
        if root.left == None and root.right == None: return
    
        if root.right != None:
            if len(self.views) < depth+1: self.views.append(root.right.val)
            self.traverse(root.right, depth+1)
            
        if root.left != None:
            if len(self.views) < depth+1: self.views.append(root.left.val)
            self.traverse(root.left, depth+1)
        