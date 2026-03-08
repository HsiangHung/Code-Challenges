## [Leetcode#450] Delete Node in a BST
#   
#  Uber
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_min(self, parent, node):
        if node.left:
            return self.get_min(node, node.left)
        # We found the successor! 
        # Before we return it, we must detach it from its parent
        if parent.left == node:
            parent.left = node.right # Successor might have a right child
        else:
            parent.right = node.right
            
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        def search_node(parent, node, key):
            """
            binary search the node first
            """
            if not node:
                return None, None
            if node.val == key:
                return parent, node
            elif node.val > key:
                return search_node(node, node.left, key)
            elif node.val < key:
                return search_node(node, node.right, key)

        parent, node = search_node(None, root, key)
        if node is None: # if didn't find the node == key
            return root

        if node.left and node.right: 
            # if node exists both left and right, replaced by min of right branch
            new_node = self.get_min(node, node.right)
            new_node.left = node.left
            new_node.right = node.right
        elif node.left and not node.right:
            # if node exists left only, replaced by node.left
            new_node = node.left
        elif not node.left and node.right:
            # if node exists right only, replaced by node.right
            new_node = node.right
        else:
            new_node = None
        if node == root:
            return new_node
        
        if node == parent.right :
            parent.right = new_node
        else:
            parent.left = new_node
        
        return root 