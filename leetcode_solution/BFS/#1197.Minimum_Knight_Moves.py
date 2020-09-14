# #1197. Minimum Knight Moves
#
class Solution:        
    def minKnightMoves(self, x: int, y: int) -> int:
        '''
        from discussion, using BFS is the best strategy to find minimum steps. 
        https://www.jasonjson.com/archivers/minimum-knight-moves.html
        
        record visited spots, and record at visited spots and the needed steps from (0,0)
        '''
        
        if x == 0 and y == 0: 
            return 0
        
        visited = {(0,0)}
        moves = [(0,0,0)]
        
        while moves:
            
            x1, y1, step = moves.pop(0)
                
            if x1 == x and y1 == y:
                return step
            else:
                for dx, dy in self.moving():
                    if (x1+dx, y1+dy) not in visited:
                        moves.append((x1+dx, y1+dy, step + 1))
                        visited.add((x1+dx, y1+dy))
        return -1
            
    def moving(self):
        return [(2,1), (2,-1), (1,2), (1,-2), (-2,1), (-2,-1), (-1,2), (-1,-2)]
        