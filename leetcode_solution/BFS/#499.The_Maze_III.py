#  499. The Maze III (hard)
#  https://leetcode.com/problems/the-maze-iii/
# 
class Solution:
    '''
    NOTE: once ball rolls over the hole, it can fall so stop BFS.
    So when rolling, need add additional condition: if (x,y) = hole, break iteration.

    * Put visited.add((x,y)) right after push to heap can make running time much faster!
    '''
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        
        heap = [(0, (ball[1], ball[0]), "")]
        
        ans, min_step = [], None
        
        visited = set({(ball[1], ball[0])})
        search = True
        while heap:
            
            step, (x, y), move = heapq.heappop(heap)
            
            if y == hole[0] and x == hole[1]: 
                if not min_step: min_step = step
                search = False
                ans.append((step, move))

            if not search: continue
            
            # visited.add((x, y))
            
            x2, y, dist = self.left(hole, x, y, maze)
            if x2 != x and (x2, y) not in visited: 
                visited.add((x, y))
                heapq.heappush(heap, (step+dist, (x2, y), move+"l"))

            x2, y, dist = self.right(hole, x, y, maze)
            if x2 != x and (x2, y) not in visited:
                visited.add((x, y))
                heapq.heappush(heap, (step+dist, (x2, y), move+"r"))
                
            x, y2, dist = self.up(hole, x, y, maze)
            if y2 != y and (x, y2) not in visited: 
                visited.add((x, y))
                heapq.heappush(heap, (step+dist, (x, y2), move+"u"))
            
            x, y2, dist = self.down(hole, x, y, maze)
            if y2 != y and (x, y2) not in visited: 
                visited.add((x, y))
                heapq.heappush(heap, (step+dist, (x, y2), move+"d"))
        
        ans = sorted([x[1] for x in ans if x[0] == min_step])
        
        return "impossible" if ans == [] else ans[0]
        
        
        
    def left(self, hole, x, y, maze):
        x2 = x
        while x2 > 0 and maze[y][x2-1] == 0 and (x2, y) != (hole[1], hole[0]):
            x2 -= 1
        return x2, y, abs(x2-x)

    def right(self, hole, x, y, maze):
        x2 = x
        while x2 < len(maze[0])-1 and maze[y][x2+1] == 0 and (x2, y) != (hole[1], hole[0]):
            x2 += 1
        return x2, y, abs(x2-x)
                       
    def up(self, hole, x, y, maze):
        y2 = y
        while y2 > 0 and maze[y2-1][x] == 0 and (x, y2) != (hole[1], hole[0]):
            y2 -= 1
        return x, y2, abs(y2-y) 
                                                                
    def down(self, hole, x, y, maze):
        y2 = y
        while y2 < len(maze)-1 and maze[y2+1][x] == 0 and (x, y2) != (hole[1], hole[0]):
            y2 += 1
        return x, y2, abs(y2-y)                      
        