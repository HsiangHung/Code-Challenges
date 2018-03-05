# [#129] Sum Root to Leaf Numbers
#
#
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        paths = self.traversal("", root)
        return sum([int(x) for x in paths])
    
    def traversal(self, path, root):
        if not root.left and not root.right:
            path += str(root.val)
            print path
            return [path]
        
        paths = []
        if root.left:
            paths += self.traversal(path+str(root.val), root.left)
            
        if root.right:
            paths += self.traversal(path+str(root.val), root.right)
        
        return paths