# [#94] Binary Tree Inorder Traversal
#
#
# iteration for inorder tree traversal
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root: return []

        inorder_traversal = []
 
        nodeStack = []
        done = False
   
        while not done:
         
            if root != None:
                nodeStack.append(root)
                root = root.left
            else:
                if len(nodeStack) > 0:
                    root = nodeStack.pop()
                    inorder_traversal.append(root.val)
                    root = root.right
                else:
                    done = True
                
        return inorder_traversal