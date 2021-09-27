#  1650. Lowest Common Ancestor of a Binary Tree III (medium)
#  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        arr_p, arr_q = self.DFS(p), self.DFS(q)
        arr_q = set(arr_q)
        
        for node in arr_p:
            if node in arr_q:
                return node
        
        return None
        
    
    def DFS(self, root):
        if not root: return []
        return [root] + self.DFS(root.parent)
        
            