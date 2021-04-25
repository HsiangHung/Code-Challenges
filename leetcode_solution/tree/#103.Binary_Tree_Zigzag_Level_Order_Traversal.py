#  103. Binary Tree Zigzag Level Order Traversal (medium)
#  https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        queue = [(root, 0)]
        ans = []
        while queue:
            
            node, layer = queue.pop(0)
            
            if len(ans) < layer + 1:
                ans.append([node.val])
            else:
                ans[layer].append(node.val)
                
            if node.left: 
                queue.append((node.left, layer + 1))
                
            if node.right: 
                queue.append((node.right, layer + 1))
        
        
        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i] = ans[i][::-1]
        
        return ans