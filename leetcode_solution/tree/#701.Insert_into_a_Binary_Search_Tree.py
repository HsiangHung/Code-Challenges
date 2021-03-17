#  701. Insert into a Binary Search Tree (medium)
#  https://leetcode.com/problems/insert-into-a-binary-search-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    https://leandrotk.github.io/series/algorithms-problem-solving/insert-into-binary-search-tree.html
    '''
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val=val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
