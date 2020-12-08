#  1382. Balance a Binary Search Tree (medium)
#  https://leetcode.com/problems/balance-a-binary-search-tree/
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root: return []
        array = self.get_array(root)
        return self.DFS(array)
        
    def DFS(self, array):
        if len(array) == 0: return None
        if len(array) == 1: return TreeNode(val=array[0])
        mid = len(array) // 2
        root = TreeNode(array[mid])
        root.left = self.DFS(array[:mid])
        root.right = self.DFS(array[mid+1:])
        return root
        
    def get_array(self, root):
        if not root: return []
        ans = self.get_array(root.left)
        ans += [root.val]
        ans += self.get_array(root.right)
        return ans