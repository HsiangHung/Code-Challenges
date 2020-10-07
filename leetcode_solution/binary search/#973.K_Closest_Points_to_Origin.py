# #973. K Closest Points to Origin
#
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        '''
        NOTE for this problem, when insert distance, needs to use binary search.
        if use simple sesarch, time exceed for more points test case.
        https://blog.csdn.net/MrJustin/article/details/106464272
        '''     
        queue = []
        
        for point in points:
            dist = point[0]**2+point[1]**2
            if queue == []:
                queue.append([dist, point])
            else:
                if len(queue) < K:
                    queue = self.insert_point_queue(dist, point, queue)
                else:
                    if dist <= queue[0][0]:
                        queue.insert(0, [dist, point])
                    elif queue[-1][0] > dist > queue[0][0]:
                        queue = self.insert_point_queue(dist, point, queue)
                        
                    queue = queue[:K]
                    
        return [x[1] for x in queue]
                
                
                
    def insert_point_queue(self, dist, point, queue):
        
        if dist <= queue[0][0]:
            queue.insert(0, [dist, point])
        elif dist > queue[-1][0]:
            queue.append([dist, point])
        else:  
            # i = self.simple_search(dist, queue)
            # queue.insert(i, [dist, point])
            
            i = self.binary_search(0, dist, queue)
            queue.insert(i+1, [dist, point])  ## NOTE here we insert i+1
        return queue
    
    
    def binary_search(self, offset, val, queue):

        if len(queue) == 1: return offset
        
        i = int((len(queue)-1)/2)
            
        if queue[i][0] <= val < queue[i+1][0]: 
            return i + offset
        elif val >= queue[i][0]:
            return self.binary_search(offset+i, val, queue[i:])
        elif val < queue[i][0]:
            return self.binary_search(offset, val, queue[:i+1])


    def simple_search(self, val, queue):
        i = 0
        while i < len(queue) and val > queue[i][0]:
            i += 1
        return i