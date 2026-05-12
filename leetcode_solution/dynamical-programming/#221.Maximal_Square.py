#  221. Maximal Square (medium)
#  https://leetcode.com/problems/maximal-square/
#
class Solution:
    '''
    use dynamical programming. dp is 2D array
    [["1","0","1","0","0"],         dp = 1 0 1 0 0
     ["1","0","1","1","1"],              1 0 1 1 1
     ["1","1","1","1","1"],              1 1 1 2 2
     ["1","0","0","1","0"]]              1 0 0 1 0
     
        dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1 if matrix[y][x] == "1" 
     or dp[y][x] = 0 if matrix[y][x] == "0" 
     
     maximal_square is determined by minimum length of x, y,diagonal direction. 
     
    '''
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        max_length = 0
        
        dp = []
        for _ in range(len(matrix)):
            dp.append([0]*len(matrix[0]))
            
        for y in range(len(matrix)):
            dp[y][0] = int(matrix[y][0])
            max_length = max(max_length, dp[y][0])
            
        for x in range(len(matrix[0])):
            dp[0][x] = int(matrix[0][x])
            max_length = max(max_length, dp[0][x])

        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[0])):
                if matrix[y][x] == "0":
                    dp[y][x] = 0
                else:
                    dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1
                    max_length = max(max_length, dp[y][x])
                    
        return max_length**2