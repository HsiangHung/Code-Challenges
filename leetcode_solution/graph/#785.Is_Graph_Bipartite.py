# 785. Is Graph Bipartite? (medium)
# https://leetcode.com/problems/is-graph-bipartite/
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
        edges = {}
        for i in range(len(graph)):
            edges[i] = graph[i]
        
        visited = [0]*len(edges)
                
        self.bipartite = True
        
        for node in range(len(visited)):
            if visited[node] == 0:
                visited[node] = 1
                self.DFS(node, visited, edges)
        return self.bipartite
            
    def DFS(self, n, visited, edges):        
        for x in edges[n]:
            if visited[x] == 0:
                visited[x] = self.flip_color(visited[n])
                self.DFS(x, visited, edges)
            else:
                if visited[x] != self.flip_color(visited[n]):
                    self.bipartite = False
                    return 
                    
    def flip_color(self, color):
        return -1 if color == 1 else 1


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