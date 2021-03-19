#  286. Walls and Gates (medium)
#  https://leetcode.com/problems/walls-and-gates/
#
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        '''
        https://www.cnblogs.com/grandyang/p/5285868.html
        '''
        for y in range(len(rooms)):
            for x in range(len(rooms[0])):
                if rooms[y][x] == 0:
                    self.DFS(x, y, rooms, 0)
        return rooms            
        
        
    def DFS(self, x, y, rooms, step):
        if rooms[y][x] == -1: return 
        
        if rooms[y][x] > 0:
            if step > rooms[y][x]: return
            rooms[y][x] = step
            
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if len(rooms[0]) > dx + x >= 0 and len(rooms) > dy + y >= 0 and rooms[y+dy][x+dx] > 0:
                self.DFS(x+dx, y+dy, rooms, step + 1)
        