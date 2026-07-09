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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        ref: https://www.youtube.com/watch?v=LFzAoJJt92M&t=75s
        part of code is optimized by Claude
        """
        if not root:
            return None

        def get_min_node(node):
            if not node.left:
                return node
            return get_min_node(node.left)

        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left and root.right:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                successor = get_min_node(root.right)
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
                return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            root.right = self.deleteNode(root.right, key)
            return root