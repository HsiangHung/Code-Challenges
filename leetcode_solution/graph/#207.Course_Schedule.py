# #207. Course Schedule
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        '''
        https://www.youtube.com/watch?v=qe_pQCh09yU
        https://www.youtube.com/watch?v=kXy0ABd1vwo
        topological sorting. DAG: directed acyclic diagram
        O(V+E) V:vertex, E: edge
        good test examples:
        * [[1,0], [2,1], [3,2], [0,3]],  cyclic
        * [[2,5],[0,5],[2,4],[1,4],[1,3],[3,0],[2,0]], sort = [5,4,0,2,3,1]
        '''
    
        self.flag = False  # if self.flag is true, there is cyclic in the graph
        visited = [0]*numCourses
        
        courses = {}
        for x in prerequisites:
            courses[x[1]] = courses.get(x[1], []) + [x[0]] # (a, b): b -> a
        
        for i in range(numCourses):
            self.DFS(i, numCourses, visited, courses)
            
        return not self.flag 
                
        
    def DFS(self, i, numCourses, visited, courses):
        '''
        visited[i] = 0: unvisited, 
        visited[i] = 2: visited but processing
        visited[i] = 1: visited and processed (been retreat back)
        
        if graph is propogating and see visited[i] = 2, means there is cycling.
        '''
        if visited[i] != 0:
            if visited[i] == 2: self.flag = True
            return
             
        visited[i] = 2
                
        if i in courses:
            for x in courses[i]:
                # NOTE, whatever, still need to try visit to get visited[i] 
                self.DFS(x, numCourses, visited, courses)
                    
        if visited[i] == 2:
            visited[i] = 1
        
