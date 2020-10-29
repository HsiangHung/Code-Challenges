## [#114] Flatten Binary Tree to Linked List
#
#  Microsoft
#
class Solution(object):
     def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        if not root.left and not root.right: return root
                
        left, right = root.left, root.right
        
        if left:
            root.right = left
            root.left = None
            left = self.flatten(left) 
            if right:
                left.right = right
                right = self.flatten(right)
                return right
            else:
                return left
        else:
            if right: return self.flatten(right)

        # if left and right:
        #     root.right = left
        #     root.left = None
        #     left = self.flatten(left)            
        #     left.right = right
        #     right = self.flatten(right)
        #     return right
        # elif left and not right:
        #     root.right = left
        #     root.left = None
        #     left = self.flatten(left)
        #     return left
        # elif not left and right:  # note, this is necessary since we need to come back last node for later concat.
        #     return self.flatten(right)
        
        return right               