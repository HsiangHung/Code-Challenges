# [#652]  Find Duplicate Subtrees
#
# Google
#
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root: return []
        self.subTree, self.duplicate = {}, set({})
        
        self.traversal(root)

        print self.subTree
        
        return list(self.duplicate)
        
    def traversal(self, root):
        if not root.left and not root.right:
            if str(root.val) in self.subTree and self.subTree[str(root.val)] == 1:
                self.duplicate.add(root)
            self.subTree[str(root.val)] = self.subTree.get(str(root.val), 0) + 1
            return str(root.val)
        
        path = str(root.val)
        if root.left:
            path += ','+self.traversal(root.left)
        else:
            path += ',null'  ## consider subtree [1,null,2] is different [1,2,null]
        
        if root.right:
            path += ','+self.traversal(root.right)
    
        if path in self.subTree and self.subTree[path] == 1:
            self.duplicate.add(root)
            
        self.subTree[path] = self.subTree.get(path, 0) + 1
        
        return path
        