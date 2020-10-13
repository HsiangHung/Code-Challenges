# 1008. Construct Binary Search Tree from Preorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        '''
        using stack. Whenever a new node, push into stack.
        if preorder[i] > stack[-1], means right child and needs to pop
        until preorder[i] < stack[-1].
        '''
        root = TreeNode(val=preorder[0])
        stack = [root]
        
        idx = 1
        node = root
        while idx < len(preorder):
            child = TreeNode(val=preorder[idx])
            if preorder[idx] < stack[-1].val:
                stack.append(child)
                node.left = child
                node = node.left
            else:
                while len(stack) > 0 and preorder[idx] > stack[-1].val:
                    prev = stack.pop()
                prev.right = child
                stack.append(child)
                node = prev.right                
                
            idx += 1
            
        return root