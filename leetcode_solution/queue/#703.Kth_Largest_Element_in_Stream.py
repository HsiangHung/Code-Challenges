# #703. Kth Largest Element in a Stream
# 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.queue = sorted(nums)[-k:]
        self.k = k
        

    def add(self, val: int) -> int:
        if len(self.queue) == 0:
            self.queue.append(val)
        else:
            if val > self.queue[-1]:
                self.queue.append(val)
            elif val < self.queue[0]:
                self.queue.insert(0, val)
            else:
                i = 0
                while i <= len(self.queue)-1 and val > self.queue[i]:
                    i += 1

                self.queue.insert(i, val)
        
            self.queue = self.queue[-self.k:]
        
        return self.queue[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)