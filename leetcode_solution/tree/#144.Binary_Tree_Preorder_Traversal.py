# #144 Binary Tree Preorder Traversal
#
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
        
        preorder = []
        
        if not root: return preorder
        
        stack = [root]
        while len(stack) != 0:
            node = stack.pop(0)
            
            preorder.append(node.val)
            #print node.val
            if node.right:
                stack.insert(0, node.right)
                
            if node.left:
                stack.insert(0, node.left)
                
        return preorder