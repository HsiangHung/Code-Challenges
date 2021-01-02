#  505. The Maze II (medium)
#  https://leetcode.com/problems/the-maze-ii/
#
class Solution:
    '''
    https://zhenyu0519.github.io/2020/03/22/lc505/ 
        
    NOTE for such shortest distance problem, use heap. Use BFS only cannot gaurantee to get 
    shortest distance. i.e. Solution2 doesn't work.
    '''
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        '''
        https://zhenyu0519.github.io/2020/03/22/lc505/ 
        
        such shortest distance problem needs to use heap. Use BFS cannot gaurantee to get shortest 
        distance.
        '''
        heap = [(0, (start[1], start[0]))]
        
        visited = set({})
        while heap:
            
            step, (x, y) = heapq.heappop(heap)
            
            if y == destination[0] and x == destination[1]:  return step
            
            visited.add((x, y))
            
            x2, y = self.left(x, y, maze)
            if x2 != x and (x2, y) not in visited: heapq.heappush(heap, (step+abs(x2-x), (x2, y)))

            x2, y = self.right(x, y, maze)
            if x2 != x and (x2, y) not in visited: heapq.heappush(heap, (step+abs(x2-x), (x2, y)))
                
            x, y2 = self.up(x, y, maze)
            if y2 != y and (x, y2) not in visited: heapq.heappush(heap, (step+abs(y2-y), (x, y2)))
            
            x, y2 = self.down(x, y, maze)
            if y2 != y and (x, y2) not in visited: heapq.heappush(heap, (step+abs(y2-y), (x, y2)))
                     
        return -1


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



class Solution2:
    '''
    NOTE this sol only uses BFS, and passed 69/78 test cases in Leetcode
    '''
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        BFS = [(start[1], start[0], 0)]
        
        visited = set({})
        while BFS:
            
            x, y, step = BFS.pop(0)
                
            if y == destination[0] and x == destination[1]: 
                return step
            
            visited.add((x, y))
            
            x2, y = self.left(x, y, maze)
            if x2 != x and (x2, y) not in visited: BFS.append((x2, y, step+abs(x2-x)))

            x2, y = self.right(x, y, maze)
            if x2 != x and (x2, y) not in visited: BFS.append((x2, y, step+abs(x2-x)))
                
            x, y2 = self.up(x, y, maze)
            if y2 != y and (x, y2) not in visited: BFS.append((x, y2, step+abs(y2-y)))
            
            x, y2 = self.down(x, y, maze)
            if y2 != y and (x, y2) not in visited: BFS.append((x, y2, step+abs(y2-y)))
                     
        return -1
