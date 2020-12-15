# 1091. Shortest Path in Binary Matrix (medium)
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
#
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        such problem is similar to: 1197. Minimum Knight Moves
        We can use DFS to go through all possible paths, but time exceeds.
        We need to use BFS here. remember to pop(0), deal with first-come path
        also immediate update it next step. 
        If update grid[y2][x2] = step+1 on line 19, we will spend a lot time to run
        duplicated paths.
        '''
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1] == 1: return -1
        
        queue = [(0, 0, 1)]
        visited = set({(0, 0)})
        
        while queue:
            x, y, step = queue.pop(0)
            if x == len(grid[0])-1 and y == len(grid)-1: return step
        
            for x2, y2 in self.move(len(grid[0]), len(grid), x, y):
                if grid[y2][x2] != 1 and (x2, y2) not in visited:
                    queue.append((x2, y2, step + 1))
                    visited.add((x2, y2))
        return -1 
    
    def move(self, m, n, x, y):
        moves = []
        for i, j in [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0, -1), (1, -1)]:
            if  0 <= x+i < m and 0 <= y+j < n:
                moves.append((x+i, y+j))
        return moves
            
       