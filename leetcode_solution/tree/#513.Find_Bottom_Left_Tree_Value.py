#[#513] Find Bottom Left Tree Value
#
#
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.leftNodes = {}
        self.traverse(0, root)
        return self.leftNodes[max([depth for depth in self.leftNodes])]
        
        
    def traverse(self, depth, root):
        
        if depth not in self.leftNodes:
            self.leftNodes[depth] = root.val
        
        if not root.left and not root.right:
            return
        
        if root.left:
            self.traverse(depth+1, root.left)
            
        if root.right:
            self.traverse(depth+1, root.right)