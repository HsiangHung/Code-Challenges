## [Leetcode#117] Populating Next Right Pointers in Each Node II
##
##
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        self.level = {}
        self.traversal(0, root)
        
    
    def traversal(self, depth, root):
        
        if depth not in self.level:
            self.level[depth] = root
        else:
            self.level[depth].next = root
            self.level[depth] = root
        
        if not root.left and not root.right:
            return
        
        if root.left:
            self.traversal(depth+1, root.left)
            
        if root.right:
            self.traversal(depth+1, root.right)