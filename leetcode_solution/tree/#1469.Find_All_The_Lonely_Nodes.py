# #1469. Find All The Lonely Nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
        lonely = []
        
        if not root or (not root.left and not root.right): return lonely
                
        lonely += self.getLonelyNodes(root.left)
        lonely += self.getLonelyNodes(root.right)
        
        if not root.left or not root.right:
            if not root.left:
                lonely += [root.right.val]
            elif not root.right:
                lonely += [root.left.val]
                
        return lonely
        
    
        