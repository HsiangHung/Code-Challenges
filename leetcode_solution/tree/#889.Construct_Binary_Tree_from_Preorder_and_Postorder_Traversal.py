#
# 889. Construct Binary Tree from Preorder and Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(preorder) == 0:
            return

        root = TreeNode(val=preorder[0])

        if len(preorder) == 1:
            return root

        left_val = preorder[1]
        left_subtree_size = postorder.index(left_val) + 1
        # e.g. preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
        # left subtree size = 3
        # left subtree [2,4,5], [4,5,2]; right subtree [3,6,7], [6,7,3]

        root.left = self.constructFromPrePost(
            preorder[1:left_subtree_size+1],
            postorder[:left_subtree_size]
        )

        root.right = self.constructFromPrePost(
            preorder[left_subtree_size+1:],
            postorder[left_subtree_size:-1]
        )

        return root
