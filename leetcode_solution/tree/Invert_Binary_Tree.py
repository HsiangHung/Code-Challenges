## [Leetcode#226] Invert Binary Tree
## 
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return 

        self.traverse(root)
        return root

        
    def traverse(self, root):
        if root.left == None and root.right == None: return
    
        if root.left != None and root.right != None:
            Left = root.left
            self.traverse(Left)
            Right = root.right
            self.traverse(Right)
            root.left = Right
            root.right = Left
        elif root.left != None and root.right == None:
            Left = root.left
            self.traverse(Left)
            root.right = Left
            root.left = None
        elif root.left == None and root.right != None:
            Right = root.right
            self.traverse(Right)
            root.left= Right
            root.right = None