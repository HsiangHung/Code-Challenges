# iteration for preorder tree traversal
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderIterative(self, root):
        """
        https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return
 
        nodeStack = [root]
   
        while(len(nodeStack) > 0):
         
            root = nodeStack.pop()
            print root.val
            if root.right is not None:
                nodeStack.append(root.right)
                
            if root.left is not None:
                nodeStack.append(root.left)
                
        print nodeStack
        