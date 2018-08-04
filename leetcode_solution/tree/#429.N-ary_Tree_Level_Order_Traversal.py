## [Leetcode#429]  N-ary Tree Level Order Traversal
##
"""
# Definition for a Node.
#class Node(object):
#    def __init__(self, val, children):
#        self.val = val
#        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        self.levels = {}    
        self.traversal(root, 0)
        return self.levels.values()
    
    
    def traversal(self, root, depth):
        if not root: return
        if depth not in self.levels:
            self.levels[depth] = [root.val]
        else:
            self.levels[depth].append(root.val)
            
        for child in root.children:
            self.traversal(child, depth+1)

