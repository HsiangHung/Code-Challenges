## [Leetcode#450] Delete Node in a BST
#   
#  Uber
#
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return root
        
        if root.val == key:  ## take care if the delete node is the root
            left, right = root.left, root.right
            if left and right:
                min_node = self.get_min_node(right)
                min_node.left = left
                return right
            elif not left:
                return right
            elif not right:
                return left

        ## if the delete node is not the root, we need both prev and current nodes to 
        ## perform the cut process
        prev_delete, delete = self.binary_search(None, root, key)

        if delete:
            self.deleting(prev_delete, delete)
            
        return root
       
    def deleting(self, prev, root):
        left, right = root.left, root.right
        if prev.val > root.val:
            if left and right:
                min_node = self.get_min_node(right)
                prev.left = right
                min_node.left = left
            elif not left:
                prev.left = right
            elif not right:
                prev.left = left
        elif prev.val < root.val:
            if left and right:
                max_node = self.get_max_node(left)
                #print max_node.val
                prev.right = left
                max_node.right = right
            elif not left:
                prev.right = right
            elif not right:
                prev.right = left
            
    
    def get_min_node(self, root):
        if not root.left: return root
        if root.left:
            return self.get_min_node(root.left)
        
    def get_max_node(self, root):
        if not root.right: return root
        if root.right:
            return self.get_max_node(root.right)
    
    def binary_search(self, prev, root, key):
        if root.val == key: return prev, root
        
        if not root.left and not root.right: return None, None
        
        if root.val > key:
            return self.binary_search(root, root.left, key)
        elif root.val < key:
            return self.binary_search(root, root.right, key)
            
        