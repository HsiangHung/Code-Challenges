#[Leetcode#606] Construct String from Binary Tree
#
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if not node.left and not node.right:
                return f"({node.val}"

            res = f"({node.val}"
            if node.left:
                res += f"{dfs(node.left)})"
            else:
                res += f"()"

            if node.right:
                res += f"{dfs(node.right)})"

            return res

        return dfs(root)[1:] # root val doesn't need "(" and ")" in the end