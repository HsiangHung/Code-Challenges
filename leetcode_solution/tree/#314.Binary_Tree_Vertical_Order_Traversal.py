#  314. Binary Tree Vertical Order Traversal
#  https://leetcode.com/problems/binary-tree-vertical-order-traversal/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.order = {}
        
        queue = [(root, 0)]
        while queue:    
            node, x = queue.pop(0)
            self.order[x] = self.order.get(x, []) + [node.val]
            
            if node.left:
                queue.append((node.left, x-1))
                
            if node.right:
                queue.append((node.right, x+1))
                
        return [self.order[x] for x in sorted(self.order.keys())]
        