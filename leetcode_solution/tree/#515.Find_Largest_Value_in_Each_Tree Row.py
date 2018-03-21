# [#515] Find Largest Value in Each Tree Row
#
# 
#
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        self.max_node = []
        self.traversal(0, root)
        return self.max_node
    
    def traversal(self, depth, root):
        
        if len(self.max_node) < depth+1:
            self.max_node.append(root.val)
        else:
            self.max_node[depth] = max(self.max_node[depth], root.val)
        
        if not root.left and not root.right:
            return
        
        if root.left:
            self.traversal(depth+1, root.left)
            
        if root.right:
            self.traversal(depth+1, root.right)
        