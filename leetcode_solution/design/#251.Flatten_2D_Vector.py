#  251. Flatten 2D Vector (medium)
#  https://leetcode.com/problems/flatten-2d-vector/
#
class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.data = self.flatten(vec)
        self.pointer = 0

    def next(self) -> int:
        x = self.data[self.pointer]
        self.pointer += 1
        return x
        
    def hasNext(self) -> bool:
        return self.pointer < len(self.data)
    
    def flatten(self, vec):
        ans = []
        for x in vec:
            if len(x) == 1:
                ans.append(x[0])
            else:
                ans += x
        return ans


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()