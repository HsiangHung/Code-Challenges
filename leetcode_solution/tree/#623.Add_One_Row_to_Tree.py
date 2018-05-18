## [#623] Add One Row to Tree
#   
#  Gilbilt
#
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root: return root
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        return self.traversal(1, root, v, d)
        
    def traversal(self, depth, root, v, d):
        if depth == d-1:

            left, right = root.left, root.right
            root.left, root.right = TreeNode(v), TreeNode(v)
            
            if left:
                root.left.left = left
                
            if right: 
                root.right.right = right

        
        if not root.left and not root.right:
            return
        
        if root.left:
            self.traversal(depth+1, root.left, v, d)
            
        if root.right:
            self.traversal(depth+1, root.right, v, d)
            
        return root