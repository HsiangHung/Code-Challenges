#  417. Pacific Atlantic Water Flow (medium)
#  https://leetcode.com/problems/pacific-atlantic-water-flow/
#
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        ans = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):

                self.pacific, self.atlantic= False, False
                self.DFS(x, y, matrix, set({}))
                
                if self.pacific and self.atlantic:
                    ans.append([y, x])
        
        return ans
    
    def DFS(self, x, y, matrix, visited):
        
        if (x, y) in visited: return
        
        if x == 0 or y == 0: self.pacific = True
        if x == len(matrix[0])-1 or y == len(matrix)-1: self.atlantic= True
        
        visited.add((x, y))
        
        if x > 0 and matrix[y][x-1] <= matrix[y][x]:
            self.DFS(x-1, y, matrix, visited)
                
        if y > 0 and matrix[y-1][x] <= matrix[y][x]:
            self.DFS(x, y-1, matrix, visited)
                
        if x < len(matrix[0])-1 and matrix[y][x+1] <= matrix[y][x]:
            self.DFS(x+1, y, matrix, visited)
                
        if y < len(matrix)-1 and matrix[y+1][x] <= matrix[y][x]:
            self.DFS(x, y+1, matrix, visited)
                
