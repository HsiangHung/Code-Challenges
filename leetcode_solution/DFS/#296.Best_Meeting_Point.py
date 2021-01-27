#  296. Best Meeting Point (hard)
#  https://leetcode.com/problems/best-meeting-point/
#
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        mx, ny = len(grid[0]), len(grid)
        
        people = set([])
        for y in range(ny):
            for x in range(mx):
                if grid[y][x] == 1:
                    people.add((x, y))
                
        # prepare dictionary where keys are people's locations to origin (0,0)
        dist = {}
        for x, y in people:
            dist[(x, y)] = x+y      
        
        self.min_dist = sum(dist.values())
        
        self.DFS(mx, ny, 0, 0, self.min_dist, people, set({}))
        
        return self.min_dist

    
    def DFS(self, mx, ny, x, y, dist, people, visited):
        '''
        DFS for all locations. We start from (0,0), and only need to know relative change to the
        distance sum. If distance > mininum, stop sesrch.
        '''
        if (x, y) in visited or dist > self.min_dist: return # trick: return when dist > minimum
        
        visited2 = visited.copy()
        visited2.add((x, y))
        
        self.min_dist = min(self.min_dist, dist)
        
        if x > 0 and (x-1, y) not in visited2:
            self.DFS(mx, ny, x-1, y, dist + self.distance_change(x, x-1, y, y, people), people, visited2)
         
        if y > 0 and (x, y-1) not in visited2:
            self.DFS(mx, ny, x, y-1, dist + self.distance_change(x, x, y, y-1, people), people, visited2)
  
        if x < mx-1 and (x+1, y) not in visited:
            self.DFS(mx, ny, x+1, y, dist + self.distance_change(x, x+1, y, y, people), people, visited2)
  
        if y < ny-1 and (x, y+1) not in visited:
            self.DFS(mx, ny, x, y+1, dist + self.distance_change(x, x, y, y+1, people), people, visited2)
  
            
    def distance_change(self, x1, x2, y1, y2, people):
        '''
        find relative total change in distance by moving (x1, y1) -> (x2, y2)
        '''
        dx, dy = x2 - x1, y2 - y1

        d_dist = 0
        for px, py in people:
            
            if dx > 0:
                if x2 <= px:
                    d_dist -= dx
                elif x1 >= px:
                    d_dist +=  dx
            elif dx < 0:
                if x2 >= px:
                    d_dist -= abs(dx)
                elif x1 <= px:
                    d_dist += abs(dx)
             
            if dy > 0:
                if y2 <= py:
                    d_dist -= dy
                elif y1 >= py:
                    d_dist += dy
            elif dy < 0:
                if y2 >= py:
                    d_dist -= abs(dy)
                elif y1 <= py:
                    d_dist += abs(dy)
      
        return d_dist
