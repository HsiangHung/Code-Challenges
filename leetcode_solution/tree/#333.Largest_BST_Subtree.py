#  333. Largest BST Subtree (medium)
#  https://leetcode.com/problems/largest-bst-subtree/
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        '''
        in the example of [10,5,15,1,8,null,7]:
        
              10
             /  \
            5   15
           / \    \
          1   8    7
          
          
        subtree [5,1,8] is a BST. But root 10 doesn't have a BST since [15,7] is not a BST.
        
        for root to have sub BST:
        (1) max of left subtree < root < min of right subtree 
        (2) both left and right subtrees are BST.
        If either of above is not satisfied, we return sub BST size = 0
        '''
        if not root: return 0
        
        self.max_size = 1
        self.search = True
        
        _, _, _ = self.DFS(root)
        return self.max_size
        
        
    def DFS(self, root):
        if not root.left and not root.right: 
            self.search = True
            return root.val, root.val, 1
        
        subTree = 0  # initally assume subtree size = 0
        if root.left and root.right:
            minLeft, maxLeft, size_L = self.DFS(root.left)
            minRight, maxRight, size_R = self.DFS(root.right)
            if size_L > 0 and size_R > 0 and maxLeft < root.val < minRight: subTree = size_L + size_R + 1
        elif root.left:
            minLeft, maxLeft, size_L = self.DFS(root.left)
            if size_L > 0 and maxLeft < root.val: subTree = size_L + 1
            maxRight = max(maxLeft, root.val)
        elif root.right:
            minRight, maxRight, size_R = self.DFS(root.right)
            if size_R > 0 and root.val < minRight: subTree = size_R + 1
            minLeft = min(minRight, root.val)
        
        if subTree > 0: self.max_size = max(self.max_size, subTree)  # trick!
            
        return minLeft, maxRight, subTree
    
    