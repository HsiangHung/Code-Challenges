#  305. Number of Islands II (hard)
#  https://leetcode.com/problems/number-of-islands-ii/
#
class Solution:
    '''
    ** I feel this version is easier to understand than hash table verion:
       https://github.com/HsiangHung/Code-Challenges/blob/master/leetcode_solution/hash%20table/%23305.Number_of_Islands_II.py

    e.g. [[0,0], [0,1], [1,2], [2,1], [2,2], [1,1]], ans = [1,1,2,3,2,1] 
    
                  1 1 0     1 1 0      1 1 0
         we have  0 0 2 =>  0 0 2  =>  0 1 1
                  0 3 0     0 2 2      0 1 1
                                              
                                  
         we need to check if (x +/- 1,y), (x, y +/- 1) have been labeled. If yes, merge the labels (using DFS).
         
         NOTE the island label index "num_island" always increases, since island index merge happens.
         everytime merge happens, remove the grid[y][x] and always fill min_val
         the number of islands = len(self.island_tag)
    '''
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        grid = []
        for _ in range(m):
            grid.append([0]*n)
        
        ans = []
        
        num_islands = 0
        self.island_tag = set({})
        for y, x in positions:
            if grid[y][x] == 0:
                
                neighbors = set({})
                for x2, y2 in self.neighbor(m, n, x, y):
                    neighbors.add(grid[y2][x2])

                if sum(list(neighbors)) == 0:
                    num_islands += 1
                    grid[y][x] = num_islands
                    self.island_tag.add(num_islands)
                else:
                    min_label = min([x for x in neighbors if x > 0])
                    grid[y][x] = min_label
                    self.DFS(m, n, x, y, grid, min_label)
                    
            ans.append(len(self.island_tag))
        
        return ans
            
        
    def DFS(self, m, n, x, y, grid, min_label):       
        if grid[y][x] in self.island_tag and grid[y][x] > min_label: 
            self.island_tag.remove(grid[y][x])
        
        grid[y][x] = min_label
        
        if x > 0 and grid[y][x-1] > min_label:
            self.DFS(m, n, x-1, y, grid, min_label)
            
        if y > 0 and grid[y-1][x] > min_label:
            self.DFS(m, n, x, y-1, grid, min_label)
     
        if x < n-1 and grid[y][x+1] > min_label:
            self.DFS(m, n, x+1, y, grid, min_label)
        
        if y < m-1 and grid[y+1][x] > min_label:
            self.DFS(m, n, x, y+1, grid, min_label)
            
    def neighbor(self, m, n, x, y):
        neighbors = []
        for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            if n > x + dx >= 0 and m > y + dy >= 0:
                neighbors.append((x+dx, y+dy))
        return neighbors            
            