#  938. Range Sum of BST (easy)
#  https://leetcode.com/problems/range-sum-of-bst/
#  
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        '''
        time O(n) n: numb of nodes
        '''
        if not root: return 0
        
        Sum = 0
        if low <= root.val <= high:
            Sum += root.val
            
        return Sum + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)



# if tree is big, we can optimize as follows:
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        '''
        For BST:
        if root > high, we don't have to traverse right branch (but still need root.left)
        if root < low, we don't have to traverse left branch (but still need root.right)
        '''
        if not root: return 0
        
        Sum = 0
        if low <= root.val <= high:
            Sum += root.val
        
        if not (root.val > high):
            Sum += self.rangeSumBST(root.right, low, high)
            
        if not (root.val < low):
            Sum += self.rangeSumBST(root.left, low, high)
        
        return Sum