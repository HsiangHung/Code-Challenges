# [#251] Flatten 2D Vector
#
#
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = []
        for vec in vec2d:
            self.vec2d += vec

    def next(self):
        """
        :rtype: int
        """
        lst = self.vec2d[0]
        self.vec2d.remove(lst)
        return lst
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.vec2d) > 0
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())