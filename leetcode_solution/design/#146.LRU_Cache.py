#  146. LRU Cache (medium)
#  https://leetcode.com/problems/lru-cache/
#
#  We need to use double linked list, to perform the linked hashmap (sort dictionary)
#  https://www.youtube.com/watch?v=akFRa58Svug (tech code Youtube)
#  https://baihuqian.github.io/2018-06-20-lru-cache/
#
class Node(object):
    '''
    double linked list
    '''
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

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

    We need to use double linked list, to perform the linked hashmap (sort dictionary)
    https://www.youtube.com/watch?v=akFRa58Svug (tech code Youtube)
    https://baihuqian.github.io/2018-06-20-lru-cache/
    '''
    def __init__(self, capacity: int):
        
        self.dict = {} # dictionary to store double linked list nodes
        self.cap = capacity
        self.head = None
        self.tail = None
        self.list_len = 0
        
    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            node = self.dict[key]
            if node != self.tail:
                self.removeNode(node)   # need to remove this node from the linked-list
                self.addNode(node)     # and then insert to tail     
            return node.val

    def put(self, key: int, value: int) -> None:
                
        if self.head is None:
            self.head = self.tail = Node(key, value)
            self.head.next, self.tail.next = self.tail, self.head
            self.head.prev, self.tail.prev = self.tail, self.head
            self.dict[key] = self.head
            self.list_len = 1
        else:
            if key not in self.dict:
                new_node = Node(key, value)
                self.addNode(new_node)
                self.dict[new_node.key] = new_node                
                if len(self.dict) > self.cap:
                    remove_node = self.head
                    self.removeNode(remove_node)
                    del self.dict[remove_node.key]
                
            else:
                node = self.dict[key]
                node.val = value
                self.dict[key] = node
                if node != self.tail:  ## note, we update list only the get node is not tail
                    self.removeNode(node)
                    self.addNode(node)

    def addNode(self, new_node):
        new_node.next = self.head
        new_node.prev = self.tail
        self.tail.next = new_node
        self.head.prev = new_node
        self.tail = new_node
        
    def removeNode(self, old_node):
        prev_node, next_node = old_node.prev, old_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        if old_node == self.head: self.head = next_node
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)