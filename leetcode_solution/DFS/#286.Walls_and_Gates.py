# #286. Walls and Gates
#
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        '''
        https://www.cnblogs.com/grandyang/p/5285868.html
        '''
        if len(rooms) == 0 or len(rooms[0]) == 0: return rooms
        
        m, n = len(rooms[0]), len(rooms)
        
        for y in range(n):
            for x in range(m):
                if rooms[y][x] == 0:
                    self.DFS(m, n, x, y, rooms, 0)
        return rooms
                    
        
    def DFS(self, m, n, x, y, rooms, distance):
                
        if distance > rooms[y][x]: return
        
        rooms[y][x] = distance
    
        
        if x > 0 and (rooms[y][x] != -1 or rooms[y][x] != 0):
            self.DFS(m, n, x-1, y, rooms, distance +1)
            
        if x < m-1 and (rooms[y][x] != -1 or rooms[y][x] != 0):
            self.DFS(m, n, x+1, y, rooms, distance +1)
       
        if y > 0 and (rooms[y][x] != -1 or rooms[y][x] != 0):
            self.DFS(m, n, x, y-1, rooms, distance +1)
            
        if y < n-1 and (rooms[y][x] != -1 or rooms[y][x] != 0):
            self.DFS(m, n, x, y+1, rooms, distance +1)
       
 