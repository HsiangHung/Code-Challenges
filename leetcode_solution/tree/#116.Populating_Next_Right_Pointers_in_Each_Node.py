## [Leetcode#116] Populating Next Right Pointers in Each Node
#
#
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return root    
        self.traversal(root.left, root.right)
        
    def traversal(self, left, right):
        if not left and not right:
            return
        
        left.next = right
        
        if left and right:
            self.traversal(left.left, left.right)
            self.traversal(right.left, right.right)
            self.traversal(left.right, right.left)
        elif left and not right:
            self.traversal(left.left, left.right)
        elif not elft and right:
            self.traversal(right.left, right.right)