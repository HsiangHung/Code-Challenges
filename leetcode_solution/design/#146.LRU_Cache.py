# # 146. LRU Cache
#
class LRUCache:
     '''
    https://www.youtube.com/watch?v=S6IfqDXWa10
    
    e.g.["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    * put [1,1]: Head (1,1) Tail
    * put [2,2]: Head (2,2), (1,1) Tail
    * get [1]: return 1 and => Head (1,1), (2,2) Tail 
    * put [3,3]: Head (3,3), (1,1) Tail
    * get [2]: return -1
    * put [4,4]: Head (4,4), (3,3) Tail
    * get [1]: return -1
    * get [3]: return 3 and => Head (3,3), (4,4) Tail
    * get [4]: return 4 and => Head (4,4), (3,3) Tail
    
    Note: when put to update existing key, also need to shift to Head.
    '''
    def __init__(self, capacity: int):
        
        self.dict = {}  # store key-value pair
        self.queue = [] # store key in order
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            self.queue.remove(key)
            self.queue.insert(0, key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.dict:
            self.dict[key] = value
            self.queue.remove(key)
            self.queue.insert(0, key)
        else:
            if len(self.queue) >= self.capacity:
                idx = self.queue.pop()
                del self.dict[idx]

            self.queue.insert(0, key)
            self.dict[key] = value
    