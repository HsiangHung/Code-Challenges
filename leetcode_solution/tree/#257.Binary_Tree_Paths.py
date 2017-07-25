## [Leetcode#257] Binary Tree Paths
## Given a binary tree, return all root-to-leaf paths.
## e.g. input: [5,4,8,11,null,13,6,7,2,null,null,null,1]
## `7->11->4->5`, `2->11->4->5`, `13->8->5`, `1->6->8->5`

#class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None        

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.paths = []
        if root: self.treePath(root, str(root.val))
        return self.paths
    
    def treePath(self, root, path):
        if not root.left and not root.right:
            self.paths.append(path)
            return 
        
        if root.left:
            self.treePath(root.left, path+'->'+str(root.left.val))
            
        if root.right:
            self.treePath(root.right, path+'->'+str(root.right.val))
        




