## [Leetcode#199] Binary Tree Right Side View
##
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class Solution(object):
## this method considers to go through right DFS first
##
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
        
        
# ----------------------------------------------------------------------------        
### method two:
    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        self.levels = []
        self.traverse(root, 1)
        return [x[0] for x in self.levels]
        
    def traverse(self, root, depth):
        if len(self.levels) < depth:
            self.levels.append([root.val])
        else:
            self.levels[depth-1].insert(0, root.val)
            
        if not root.left and not root.right: return
    
        if root.left != None: self.traverse(root.left, depth+1)
        if root.right != None: self.traverse(root.right, depth+1)