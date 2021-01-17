#  116. Populating Next Right Pointers in Each Node (medium)
#  https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return root    
        self.traversal(root.left, root.right)
        
    def traversal(self, left, right):
        if not left or not right: return
        
        left.next = right

        self.traversal(left.left, left.right)
        self.traversal(right.left, right.right)
        self.traversal(left.right, right.left)
        