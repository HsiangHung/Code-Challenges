#
#  841. Keys and Rooms
#  
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        graph = {}
        for i in range(len(rooms)):
            for key in rooms[i]:
                graph[i] = graph.get(i, []) + [key]

        visited = [False] * len(rooms)
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            if i in graph:
                for key in graph[i]:
                    dfs(key)

        dfs(0)
        return len([x for x in visited if x is True]) == len(rooms)

