#  106. Construct Binary Tree from Inorder and Postorder Traversal (medium)
#  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    similar to # 105, just root always happends on postorder[-1].
    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if len(inorder) == 0: return None
        
        val = postorder[-1]
        root = TreeNode(val=val)
        if len(inorder) == 1: return root
        
        i = self.search(inorder, val)
        
        left = self.buildTree(inorder[:i], postorder[:i])
        right = self.buildTree(inorder[i+1:], postorder[i:-1])
        
        root.left, root.right = left, right
        
        return root
        
    def search(self, arr, target):
        i = 0
        while arr[i] != target:
            i += 1
        return i