# 1091. Shortest Path in Binary Matrix
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
        if grid[0][0] !=0: return -1
        
        m = len(grid) 
        
        num_paths = 2**31-1
        
        moves = [(0, 0, 1)]
        grid[0][0] = 1
        while moves:
            y, x, step = moves.pop(0)  ## trick 1: need to pop(0), always deal eariler moves
                        
            if x == m-1 and y == m-1:
                num_paths = min(num_paths, step)       
            else:
                for x2, y2 in self.moving(m, x, y):
                    if grid[y2][x2] == 0 or (grid[y2][x2] != 1 and step+1 < grid[y2][x2]): 
                        # as long as grid not visited or has been visited but we have lower steps, update it.BufferError
                        moves.append((y2, x2, step+1))
                        grid[y2][x2] = step+1           ## trick 2: start to update grid
                        
        return num_paths if num_paths < 2**31-1 else -1
        
            
    def moving(self, m, x, y):
        moves = []
        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                x2, y2 = x+i, y+j
                if 0 <= x2 < m and 0 <= y2 < m:
                    moves.append((x2, y2))
        
        return moves