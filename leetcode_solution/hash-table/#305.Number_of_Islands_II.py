#  305. Number of Islands II (hard)
#  https://leetcode.com/problems/number-of-islands-ii/ 
#
class Solution:
    '''
    e.g. [[0,0], [0,1], [1,2], [2,1]], 
    
                  1 1 0
         we have  0 0 2, island_labels = {1:[(0,0), (0,1)], 2:[(1,2)], 3:[(2,1)]}
                  0 3 0
                                              1 1 0                    
         then if a new site is [1,1], we have 0 1 1, island_labels = {1:[(0,0),(0,1),(1,2),(2,1),(1,1)]}
                                              0 1 0
                                  
         we need to check if (x +/- 1,y), (x, y +/- 1) have been labeled. If yes, merge the labels.

         NOTE the island label index "island_" always increases, since island index merge happens.
         the number of islands = len(island_labels)

         we need store grid[y][x] = label, and island_labels = {labe:[(x, y)]}
         otherwise updating is too slow to pass tests.
    '''
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        grid = []
        for _ in range(m):
            grid.append([0]*n)
            
        ans, island_ = [], 0
        island_labels = {}        
        for row, col in positions:
            island_ = self.isIsolated(n, m, col, row, grid, island_, island_labels)
            ans.append(len(island_labels))
            
        return ans
    

    def isIsolated(self, n, m, x, y, grid, island_, island_labels):
        
        if grid[y][x] != 0: return island_
        
        isolated = set([])
        
        if x > 0 and grid[y][x-1] != 0:
            isolated.add(grid[y][x-1])
            
        if y > 0 and grid[y-1][x] != 0:
            isolated.add(grid[y-1][x])
            
        if x < n-1 and grid[y][x+1] != 0:
            isolated.add(grid[y][x+1])
                        
        if y < m-1 and grid[y+1][x] != 0:
            isolated.add(grid[y+1][x])
        
        
        if len(isolated) > 0:       # if isolated set is not empty: new site connects to labeled islands
            min_val = min(isolated)
            
            grid[y][x] = min_val
            island_labels[min_val].append((x, y))
            
            for label in isolated:  # try to update island index, considering merge to min_val
                if label != min_val:
                    for x1, y1 in island_labels[label]:
                        grid[y1][x1] = min_val
                    island_labels[min_val] += island_labels[label]
                    del island_labels[label]            
                  
        elif len(isolated) == 0:    # if isolated set is empty: new site is isolated to any labeled islands
            island_ += 1 
            island_labels[island_] = [(x, y)]
            grid[y][x] = island_      
            
        return island_