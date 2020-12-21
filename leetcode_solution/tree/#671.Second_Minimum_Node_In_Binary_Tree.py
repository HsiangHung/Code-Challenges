#  671. Second Minimum Node In a Binary Tree (easy)
#  https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    since node = min(node.left, node.right). When doing DFS, as long as node.val != root.val
    don't need to continue recursion and return.
    '''
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right): return -1
        sec_min = self.DFS(root, root.val)
        return sec_min# if sec_min != root.val else -1
        
    def DFS(self, node, min_val):        
        if node.val != min_val: return node.val 
        if not node.left and not node.right: return -1

        l_val, r_val = -1, -1
        if node.left:
            l_val = self.DFS(node.left, min_val)
        
        if node.right:
            r_val = self.DFS(node.right, min_val)
            
        if l_val != -1 and r_val != -1:
            return min(l_val, r_val)
        elif l_val != -1:
            return l_val
        elif r_val != -1:
            return r_val
        else:
            return -1