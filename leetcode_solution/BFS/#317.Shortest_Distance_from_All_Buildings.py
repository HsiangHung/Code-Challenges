#  317. Shortest Distance from All Buildings (hard)
#  https://leetcode.com/problems/shortest-distance-from-all-buildings/
#
class Solution:
    '''
    for each land, do BFS until hits building and updated distance to the buildings.
    
    This code passed 64/72 test cases
    '''
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        mx, ny = len(grid[0]), len(grid)
        
        lands, buildings = [], []
        for y in range(ny):
            for x in range(mx):
                if grid[y][x] == 1:  # building
                    buildings.append((x, y))
                elif grid[y][x] == 0: # land
                    lands.append((x, y))

        min_travel_dist = len(buildings)*(mx + ny)
        
        for lx, ly in lands:
            
            queue = [(lx, ly, 0)]
            visited = set({})
            distances = {(bx, by): mx + ny for bx, by in buildings} # for each land, we have a dist hashmap
        
            building_reach = set({})
            
            while queue and len(building_reach) < len(buildings): # BFS valid and # of building reached < total builds
                
                x, y, step = queue.pop(0)
                
                if (x, y) in visited: continue
                
                visited.add((x, y))
                
                if (x, y) in distances:
                    distances[(x, y)] = min(distances[(x, y)], step)
                    building_reach.add((x, y))
                else:
                    for x2, y2 in self.moves(mx, ny, x, y, grid):
                        if (x2, y2) not in visited:
                            queue.append((x2, y2, step + 1))
            
            if len(building_reach) == len(buildings):
                min_travel_dist = min(min_travel_dist, sum(distances.values()))

        return min_travel_dist if min_travel_dist < len(buildings)*(mx + ny) else -1
                    
                    
    def moves(self, mx, ny, x, y, grid):
        moves = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if mx > x + dx >= 0 and ny > y + dy >= 0 and grid[y+dy][x+dx] != 2:
                moves.append((x+dx, y+dy))
        return moves

