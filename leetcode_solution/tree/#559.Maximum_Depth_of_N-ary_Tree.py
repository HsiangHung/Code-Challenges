## [# 559] Maximum Depth of N-ary Tree
#
#
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        if not root: return 0
        if root.children == []: return 1
        
        max_depth = 1
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child)+1)
        
        return max_depth