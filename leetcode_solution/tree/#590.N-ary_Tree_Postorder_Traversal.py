## [Leetcode#590] N-ary Tree Postorder Traversal
##
"""
# Definition for a Node.
#class Node(object):
#    def __init__(self, val, children):
#        self.val = val
#        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        
        postorder = []
        for child in root.children:
            postorder += self.postorder(child)
        
        return postorder + [root.val]
        