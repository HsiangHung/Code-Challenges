#
# 622. Design Circular Queue
#
class MyCircularQueue:

    def __init__(self, k: int):
        self.items = []
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if len(self.items) >= self.capacity:
            return False
        else:
            self.items.append(value)
            return True

    def deQueue(self) -> bool:
        if len(self.items) > 0:
            self.items.pop(0)
            return True
        return False

    def Front(self) -> int:
        return self.items[0] if len(self.items) > 0 else -1

    def Rear(self) -> int:
        return self.items[-1] if len(self.items) > 0 else -1

    def isEmpty(self) -> bool:
        return len(self.items) == 0

    def isFull(self) -> bool:
        return len(self.items) == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()