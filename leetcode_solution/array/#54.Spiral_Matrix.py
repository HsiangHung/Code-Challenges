#
# 54. Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        path move:
        * 3x3, path [2,2,2,1,1] -> [2,2,1,1]
        * 4x4, path [3,3,3,2,2,1,1] -> [3,3,2,2,1,1]
        * 3x4, path [3,2,3,1,2] -> [2,3,1,2]

        excpet first one, start from (n-1), (m-1) and decay -1 every two
        """
        res = matrix[0]

        ny, nx = len(matrix), len(matrix[0])

        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        direct = 0
        
        x, y = nx - 1, 0
        steps = [ny - 1, nx - 1] 
        while steps[direct % 2] > 0:

            dx, dy = directions[direct % 4]
            for _ in range(steps[direct % 2]):
                x += dx
                y += dy
                res.append(matrix[y][x])

            steps[direct % 2] -= 1 
            direct += 1

        return res
