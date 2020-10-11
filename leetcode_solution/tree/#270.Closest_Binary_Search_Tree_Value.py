# # 270. Closest Binary Search Tree Value
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def closestValue(self, root: TreeNode, target: float) -> int:
        '''
        need to go through entire tree. If use the criterion < min_diff to stop,
        then we will miss another closer node under the node.
        '''
        return self.DFS(root, target)[1]
        
        
    def DFS(self, root, target):
        
        min_diff, min_node = abs(root.val-target), root.val
        
        if root.left:
            min_diff2, min_node2 = self.DFS(root.left, target)
            if min_diff2 < min_diff:
                min_diff, min_node = min_diff2, min_node2
        
        if root.right:
            min_diff2, min_node2 = self.DFS(root.right, target)
            if min_diff2 < min_diff:
                min_diff, min_node = min_diff2, min_node2
                
        return min_diff, min_node