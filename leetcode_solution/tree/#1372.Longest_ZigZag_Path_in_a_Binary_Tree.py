#
#  1372. Longest ZigZag Path in a Binary Tree
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0

        self.max_zigzag = 0
        def dfs(node, direction, step):
            self.max_zigzag = max(self.max_zigzag, step)

            if not node:
                return

            if direction == "left":
                dfs(node.left, "left", 0) # note, not 1, restart to count steps
                dfs(node.right, "right", step + 1)

            if direction == "right":
                dfs(node.left, "left", step + 1)
                dfs(node.right, "right", 0) # note, not 1, restart to count steps

        dfs(root.left, "left", 0)
        dfs(root.right, "right", 0)
        return self.max_zigzag