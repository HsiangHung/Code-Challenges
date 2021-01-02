#  490. The Maze (medium)
#  https://leetcode.com/problems/the-maze/
#
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        BFS = [(start[1], start[0])]
        
        visited = set({})
        
        while BFS:
            
            x, y = BFS.pop(0)
            
            if y == destination[0] and x == destination[1]: return True
            
            visited.add((x, y))
            
            x2, y = self.left(x, y, maze)
            if x2 != x and (x2, y) not in visited: BFS.append((x2, y))

            x2, y = self.right(x, y, maze)
            if x2 != x and (x2, y) not in visited: BFS.append((x2, y))
                
            x, y2 = self.up(x, y, maze)
            if y2 != y and (x, y2) not in visited: BFS.append((x, y2))
            
            x, y2 = self.down(x, y, maze)
            if y2 != y and (x, y2) not in visited: BFS.append((x, y2))
                     
        return False


    def left(self, x, y, maze):
        x2 = x
        while x2 > 0 and maze[y][x2-1] == 0:
            x2 -= 1
        return x2, y

    def right(self, x, y, maze):
        x2 = x
        while x2 < len(maze[0])-1 and maze[y][x2+1] == 0:
            x2 += 1
        return x2, y
                                                      
    def up(self, x, y, maze):
        y2 = y
        while y2 > 0 and maze[y2-1][x] == 0:
            y2 -= 1
        return x, y2   
                                                                
    def down(self, x, y, maze):
        y2 = y
        while y2 < len(maze)-1 and maze[y2+1][x] == 0:
            y2 += 1
        return x, y2                              
        
        