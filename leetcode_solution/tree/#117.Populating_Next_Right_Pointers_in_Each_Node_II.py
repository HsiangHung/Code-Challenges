#  117. Populating Next Right Pointers in Each Node II (medium)
#  https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
#
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


#  BFS solution
#
class BFSSolution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        
        queue = [(root, 0)]
        prev_node, prev_layer = None, -1
        while queue:
            node, layer = queue.pop(0)
            
            if node.left:
                queue.append((node.left, layer + 1))
                
            if node.right:
                queue.append((node.right, layer + 1))
            
            if layer == prev_layer: # when same layer, do .next
                prev_node.next = node
                
            prev_node = node
            prev_layer = layer
                                       
        return root
            