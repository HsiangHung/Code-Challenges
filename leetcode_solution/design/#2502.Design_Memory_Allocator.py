#
# 2502. Design Memory Allocator
#
class Allocator:

    def __init__(self, n: int):
        self.size = n
        self.block = [None] * n
        self.memory_map = {}
        

    def allocate(self, size: int, mID: int) -> int:

        put = []
        i = 0
        while i < self.size:
            if self.block[i] is None:
                put.append(i)
                if len(put) == size:
                    break
            else:
                put = []
            i += 1

        if len(put) == size:
            for i in put:
                self.block[i] = mID
                self.memory_map[mID] = self.memory_map.get(mID, []) + [i]
            return put[0]

        return -1



    def freeMemory(self, mID: int) -> int:
        if mID not in self.memory_map:
            return 0

        for i in self.memory_map[mID]:
            self.block[i] = None

        blocked_size = len(self.memory_map[mID])
        del self.memory_map[mID]
        return blocked_size
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)