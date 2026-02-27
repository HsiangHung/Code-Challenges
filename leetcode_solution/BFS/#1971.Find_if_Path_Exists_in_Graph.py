class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        if n == 1:
            return True if source == destination else False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        bfs = [source]
        while bfs:
            vertex = bfs.pop(0)
            if (visited[vertex] == True) or (vertex not in graph):
                continue

            if vertex == destination:
                return True

            visited[vertex] = True
            for x in graph[vertex]:
                if not visited[x]:
                    bfs.append(x)

        return False


