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
        if not root: return []
        self.view = []
        self.traversal(1, root)
        return self.view
    
    
    def traversal(self, depth, root):
        if len(self.view) < depth:
            self.view.append(root.val)
        else:
            self.view[depth-1] = root.val
        
        if not root.left and not root.right:
            return
        
        if root.left:
            self.traversal(depth+1, root.left)
            
        if root.right:
            self.traversal(depth+1, root.right)
        
        
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