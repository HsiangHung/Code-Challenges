#  542. 01 Matrix (medium)
#  https://leetcode.com/problems/01-matrix/
#
class Solution:
    '''
    https://www.cnblogs.com/grandyang/p/6602288.html
    
    1. default matrix[y][x] == 1 to a maximum value, like len(matrix) + len(matrix[0])
    2. prepare queue for BFS each matrix[y][x] = 0. But only select 0 which has 1 nearby.
    3. BFS only goes through matrix[y][x] = 1.
    4. During BFS, each step adds distance + 1 and if distance + 1 < matrix[y][x], update matrix[y][x]
    5. return matrix
    '''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        mx, ny = len(matrix[0])-1, len(matrix)-1
        
        queue = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    hasOneNeighbor = False
                    for x2, y2 in self.get_neighbor(x, y, mx, ny, matrix):
                        hasOneNeighbor = True
                        break
                    if hasOneNeighbor: queue.append((x, y, 0))
                else:
                    matrix[y][x] = len(matrix) + len(matrix[0]) # if val=1, initally as a maximum
                    
        while queue:
            x, y, distance = queue.pop(0)
            for x2, y2 in self.get_neighbor(x, y, mx, ny, matrix):
                if distance + 1 < matrix[y2][x2]:
                    matrix[y2][x2] = distance + 1
                    queue.append((x2, y2, distance+1))         
                    
        return matrix

    def get_neighbor(self, x, y, mx, ny, matrix):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if mx >= x + dx >= 0 and ny >= y + dy >= 0 and matrix[y+dy][x+dx] > 0:
                neighbors.append((x + dx, y + dy))
        return neighbors