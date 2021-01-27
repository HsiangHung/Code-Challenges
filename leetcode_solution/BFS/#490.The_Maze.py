#  490. The Maze (medium)
#  https://leetcode.com/problems/the-maze/
#
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        BFS = [(start[1], start[0])]
        
        visited = set({})
        
        while queue:
            x, y = queue.pop(0)
            
            if (x, y) == (destination[1], destination[0]): 
                return True
            
            visited.add((x, y))
            
            for new_loc in self.move(x, y, maze):
                if new_loc not in visited:
                    queue.append(new_loc)
            
        return False
    
    
    def move(self, x, y, maze):
        locs = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x2, y2 = x, y
            while len(maze[0]) > x2+dx >= 0 and len(maze) > y2+dy >= 0 and maze[y2+dy][x2+dx] == 0:
                x2 += dx
                y2 += dy
                
            if (x2, y2) != (x, y): locs.append((x2, y2))
                
        return locs
            
            
             
        