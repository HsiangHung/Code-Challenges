#  105. Construct Binary Tree from Preorder and Inorder Traversal (medium)
#  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    inspired by video: https://www.youtube.com/watch?v=4u9oblkt_jA
    
    The first element in preorder is always the root.
    And then we use inorder to split left and right from the root.
    e.g. preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    root = 3, 
    inorder = [9] + 3 + [15, 20, 7], preorder = 3 + [9] + [20,15,7]
    so left child must be 9, right child must be 20....
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0: return None
        
        root = TreeNode(val=preorder[0])
        
        if len(preorder) == 1: return root
                
        i = self.search(inorder, root.val)
                    
        left = self.buildTree(preorder[1:i+1], inorder[:i])
        right = self.buildTree(preorder[i+1:], inorder[i+1:])    
        
        root.left, root.right = left, right
        
        return root
            
    def search(self, arr, target):
        i = 0
        while arr[i] != target:
            i += 1
        return i
    
   