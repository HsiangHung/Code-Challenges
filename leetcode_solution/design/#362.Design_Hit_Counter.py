#  362. Design Hit Counter (medium)
#  https://leetcode.com/problems/design-hit-counter/
#
class HitCounter:

    def __init__(self):
        self.ts_queue = []
        
    def hit(self, timestamp: int) -> None:
        self.ts_queue.append(timestamp)
        while timestamp - self.ts_queue[0] >= 300:
            self.ts_queue.pop(0)

    def getHits(self, timestamp: int) -> int:
        while len(self.ts_queue) > 0 and timestamp - self.ts_queue[0] >= 300:
            self.ts_queue.pop(0)

        return len(self.ts_queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)