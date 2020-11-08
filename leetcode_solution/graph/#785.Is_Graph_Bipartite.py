# 785. Is Graph Bipartite?
#
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        * This problem I prefer to use DFS, since we may need disconnected graph.
          e.g. a test case: [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],...]
        
          we see [1,2,3,4] and [5,7,9,6] are not connected. after going through [1,2,3,4], 
          need to go through [5,6,7,9]. But due to the graphs are disconnected, we can
          assign arbitrary sign on the start_id of [5,6,7,9]
        
        * After going through a graph, check if nodes exist in graph dict. 
        * If using BFS, we may meet first meet a node as start_id and result in assigning
          its sign, but later actually it is connected to nodes visited before.
        '''
        graph = {i: graph[i] for i in range(len(graph)) if graph[i] != []}
        
        if len(graph) == 0: return True

        while len(graph) > 0:  # need to check until graph to make sure all nodes visit
            start_id = list(graph.keys())[0]
            self.visited = {start_id: 1}
            if not self.DFS(graph, start_id): return False
        return True

        
    def DFS(self, graph, id):
                                
        if id in graph:
            
            connection = graph[id]
            del graph[id]

            for neighbor in connection:
                if neighbor in self.visited:
                    if self.visited[neighbor] == self.visited[id]:
                        return False
                else:
                    self.visited[neighbor] = self.assign_color(id)
                    if not self.DFS(graph, neighbor):
                        return False
            
        return True     # important! once all nodes in the current graph visit, and
                        # all signs correct, return True

        
            
        
    def assign_color(self, i):
        if self.visited[i] == 1:
            return -1
        else:
            return 1
            


class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        This version looks a BFS, but still DFS. Two points:
        1) after node is visited and it's neighbors, immediately visit it's neighbors
        2) whne a node has not been visited, checked if this node was other visited nodes'
           neighbors. Otherwise randomly assign it's label = 1
        '''
        graph = {node:graph[node] for node in range(len(graph))}
    
        nodes = list(graph.keys())
        node = nodes.pop(0)

        visited = {}
        while nodes:
            edges = graph[node]
            
            if node not in visited:
                edgeVisited = False  # trick 1: check if node's neighbor has been visited.
                for edge in edges:
                    if edge in visited:
                        visited[node] = self.op_label(visited[edge])
                        edgeVisited = True
                        
                if not edgeVisited: visited[node] = 1
            
            for edge in edges:
                if edge in visited:
                    if visited[edge] != self.op_label(visited[node]):
                        return False
                else:
                    visited[edge] = self.op_label(visited[node])
                    nodes.remove(edge)
                    nodes.insert(0, edge)  ## trick 2: insert edge in nodes, but do soon.
            node = nodes.pop(0) 
        
        return True
            
    def op_label(self, label):
        return 1 if label == -1 else -1