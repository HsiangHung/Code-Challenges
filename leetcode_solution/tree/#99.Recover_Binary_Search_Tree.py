#  99. Recover Binary Search Tree (medium)
#  https://leetcode.com/problems/recover-binary-search-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.nodes = {}
        nodes = self.DFS(root)
                
        wrong, i = [], 1
        while i <= len(nodes)-1 and len(wrong) < 2:
            if nodes[i].val < nodes[i-1].val:
                wrong.append((i-1, i))
            i += 1

        if len(wrong) == 1:  # case I: i-1, i switch
            a, b = wrong[0]
        elif len(wrong) == 2: # case II: i, j switch, j >= i+1
            a, b = wrong[0][0], wrong[1][1]
        
        nodes[a].val, nodes[b].val = nodes[b].val, nodes[a].val
        
        return root
        
        
    def DFS(self, root):
        if not root: return []
        node = self.DFS(root.left) + [root] + self.DFS(root.right)
        return node
        
        