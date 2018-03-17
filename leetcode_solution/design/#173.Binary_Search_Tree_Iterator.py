# [# 173] Binary Search Tree Iterator
#
#
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        if root:
            self.traversal(root)
            
        self.nodeIndex = 0
        
        
    def traversal(self, root):
        if not root.left and not root.right:
            self.nodes.append(root)
            return
        
        if root.left:
            self.traversal(root.left)
            
        self.nodes.append(root)
        
        if root.right:
            self.traversal(root.right)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nodeIndex < len(self.nodes)

    def next(self):
        """
        :rtype: int
        """
        smallestNode = self.nodes[self.nodeIndex]
        self.nodeIndex += 1
        return smallestNode.val
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())