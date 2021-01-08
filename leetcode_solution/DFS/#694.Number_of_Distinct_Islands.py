#  694. Number of Distinct Islands (medium)
#  https://leetcode.com/problems/number-of-distinct-islands/
#
class Solution:
    '''
    trick: 
    1. for each island, normalized by subtracting every land in the island to (x, y)
    2. serialize the island list to string, and save into a set.
    
    e.g. 
    11000
    11000
    00011
    00011
    
    island1= [(0,0),(0,1),(1,1),(1,0)]; island2 = [(2,2),(2,3),(3,3),(3,2)]
    normalize island2 by all (x,y) - (2,2); so N(island2) = island1
    '''
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        islands = set({})
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    visited = []
                    self.DFS(x, y, grid, visited)
                    for i in range(len(visited)):
                        visited[i] = (visited[i][0]-x, visited[i][1]-y)
                    islands.add(str(visited))

        return len(islands)
        
    def DFS(self, x, y, grid, visited):
        if grid[y][x] == 0 or (x,y) in visited: return
        
        visited.append((x, y))
        grid[y][x] = 0
        
        if x > 0: self.DFS(x-1, y, grid, visited)
        
        if y > 0: self.DFS(x, y-1, grid, visited)
        
        if x < len(grid[0])-1: self.DFS(x+1, y, grid, visited)
            
        if y < len(grid)-1: self.DFS(x, y+1, grid, visited)
     