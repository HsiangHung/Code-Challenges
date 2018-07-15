## [#849] Maximize Distance to Closest Person
#
#
#

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        occupied = [i for i in range(len(seats)) if seats[i] == 1]
        
        max_dist = 0
        for i in range(1, len(occupied)):
            max_dist = max(max_dist, occupied[i]-occupied[i-1])    
        
        max_dist = max_dist // 2
        
        if seats[0] == 0:
            max_dist = max(max_dist, occupied[0])
            
        if seats[-1] == 0:
            max_dist = max(max_dist, len(seats)-1 - occupied[-1])
            
        return max_dist