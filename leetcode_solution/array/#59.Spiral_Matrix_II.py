#
# 59. Spiral Matrix II
#
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        The numbers in a sprial matrix are like:
        n, (n-1, n-1), (n-2, n-2), n-3, n-3, ....... 2, 2, 1, 1
        y=0, x=n-1, y=n-1, x=0, y=1, x=n-2, y=n-2, x=1, .....
        """

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            matrix[0][i] = i+1

        # four directions in turn: (+y), (-x), (-y), (+x)
        direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        n_loop = n - 1
        num = n
        i = 0
        x, y = n-1, 0
        while n_loop > 0:
            for iter in range(2):
                # n-1, n-1, n-2, n-2, n-3, n-3, ...... 2, 2, 1, 1, each iterates twice
                dx, dy = direction[i % 4]
                for j in range(n_loop):
                    # move +y (n-1) times, -x (n-1) times, -y (n-2) times, +x (n-2) times, ...
                    x += dx
                    y += dy
                    num += 1
                    matrix[y][x] = num
                i += 1
            n_loop -= 1

        return matrix
        
