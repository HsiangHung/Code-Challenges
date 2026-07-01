#
# 3148. Maximum Difference Score in a Grid
#
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        n_rows, n_cols = len(grid), len(grid[0])

        # this is bad solution, O(N^2 * N^2)
        # max_score = -float("inf")
        # for i in range(n_rows):
        #     for j in range(n_cols):

        #         for k in range(i, n_rows):
        #             for l in range(j, n_cols):
        #                 if (k >= i  and l > j) or (k > i  and l >= j):
        #                     max_score = max(max_score, grid[k][l]-grid[i][j])
        
        # return max_score

        """
        for A, B if need to make run, must be intercept point.
        dp[i,j] = max(
                    diff(i-1,j; i,j),
                    diff(i,j-1; i,j),
                    dp[i-1,j] + diff(i-1,j; i,j),
                    dp[i,j-1] + diff(1,j-1; i,j),
        )
        """


        dp = []
        for _ in range(n_rows):
            dp.append([-float("inf")] * n_cols)

        ans = -float("inf")
        for i in range(n_rows):
            for j in range(n_cols):
                if i == 0 and j == 0:
                    continue

                max_score = dp[i][j]
                if i > 0:
                    max_score = max(
                        max_score,
                        dp[i-1][j] + (grid[i][j]-grid[i-1][j]), 
                        grid[i][j] - grid[i-1][j]
                    )
                
                if j > 0:
                    max_score = max(
                        max_score,
                        dp[i][j-1] + (grid[i][j]-grid[i][j-1]), 
                        grid[i][j] - grid[i][j-1]
                    )
                
                dp[i][j] = max_score
                ans = max(ans, max_score)
            
        return ans