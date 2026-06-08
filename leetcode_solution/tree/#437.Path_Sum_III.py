# [# 437] Path Sum III
#  
#
#
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.res = 0
        def dfs(node, path_sums):
            """
            path_sums are list of path sum, from any nodes
            [10] -> [10+5, 10-3, 5, -3] -> ...
            """
            if not node:
                return 

            path_sums = [x + node.val for x in path_sums] + [node.val]

            for i in range(len(path_sums)):
                if path_sums[i] == targetSum:
                    self.res += 1

            dfs(node.left, path_sums)
            dfs(node.right, path_sums)

        dfs(root, [])
        return self.res
