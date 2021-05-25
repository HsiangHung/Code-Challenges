#  362. Design Hit Counter (medium)
#  https://leetcode.com/problems/design-hit-counter/
#
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.window_end = 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.data[timestamp] = self.data.get(timestamp, 0) + 1
        
        if timestamp > self.window_end:
            self.window_end = timestamp
            times = list(self.data.keys()) # if use times = self.data.keys(), it changes dict size
            
            for t in times:
                if t < timestamp - 300 + 1:
                    del self.data[t]
                    
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        
        if timestamp > self.window_end:
            
            self.window_end = timestamp
            times = list(self.data.keys())  # if use times = self.data.keys(), it changes dict size
            
            for t in times:
                if t < timestamp - 300 + 1:
                    del self.data[t]
        
        return sum([self.data[t] for t in self.data])
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)