#  538. Convert BST to Greater Tree (medium)
#  https://leetcode.com/problems/convert-bst-to-greater-tree/
#  
#  Amazon
#
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def convertBST(self, root: TreeNode) -> TreeNode:
        '''
        NOTE: to solve the problem, we have the following analysis:
        
                   parent
                  /
               root 
              /    \
           left    right
           
        It is BST, so root.val is updated as sum[right] + root's parents (if any). 
        The above tree will return the original sum by left + root.val + right
        
        So save the original sum first, and update root.val, and return the saved sum.
        '''
        if not root: return root
            
        _ = self.DFS(root, 0)
        return root
        
    def DFS(self, node, parentSum):
       
        if node.right and node.left:
            right = self.DFS(node.right, parentSum)
            left = self.DFS(node.left, parentSum + node.val + right)
            x = left + node.val + right
            node.val += parentSum + right
        elif node.right:
            right = self.DFS(node.right, parentSum)
            x = node.val + right
            node.val += parentSum + right
        elif node.left:
            left = self.DFS(node.left, parentSum + node.val)
            x = node.val + left
            node.val += parentSum
        else:
            x = node.val
            node.val += parentSum
        
        return x

#############################################################################
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        
        self.sum = 0
        self.traversal(0, root)
        return root
        
        
    def traversal(self, sum, root):
        if not root.left and not root.right:
            root.val += self.sum
            self.sum = root.val
            return
        
        if root.right:
            self.traversal(sum, root.right)
        
        root.val += self.sum
        self.sum = root.val
        
        if root.left:
            self.traversal(sum, root.left)