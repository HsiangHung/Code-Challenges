#
#  1466. Reorder Routes to Make All Paths Lead to the City Zero
#
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        ref: https://www.youtube.com/watch?v=m17yOR5_PpI

        * build a indirect (ignore arrows) and direct grap.
          e.g. dir_g = {0:[1], 1:[3], 2:[3], 4:[0,5]}
               indir_g = {0:[1], 1:[0,3], 2:[3], 3:[1,2], 4:[0,5], 5:[4]} 
        * doing BFS starting from 0 -> (1,4) -> (3, 5) -> 2:
           * first search 4 -> 0, but 1 -> 0 not exist, so + 1
           * second search 3 -> 1 not exist, 5 -> 4 not exist, so +2  
           * third search 2 -> 3 exist so +0
        1+2 = 3
        """
        indir_g, dir_g = {}, {}
        for x, y in connections:
            dir_g[x] = dir_g.get(x, []) + [y]
            indir_g[x] = indir_g.get(x, []) + [y]
            indir_g[y] = indir_g.get(y, []) + [x]
        
        ans = 0
        visited = set({})
        bfs = [0]
        while bfs:
            city = bfs.pop(0)
            visited.add(city)

            if city in indir_g:
                for nb in indir_g[city]: # nb: neighbor of city
                    if nb not in visited:
                        if (nb not in dir_g) or (city not in dir_g[nb]):
                            ans += 1
                        bfs.append(nb)
        return ans
        
        