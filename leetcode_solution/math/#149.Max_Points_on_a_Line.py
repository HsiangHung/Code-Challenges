#  149. Max Points on a Line (hard)
#  https://leetcode.com/problems/max-points-on-a-line/
#
class Solution:
    '''
    Brutal force O(n^3) => O(n^2)
    http://bookshadow.com/weblog/2014/10/16/leetcode-max-points-line/
    https://www.cnblogs.com/grandyang/p/4579693.html
    
    instead storing slopes which may have round errors, storing (y2-y1, x2-x1)
    
    example case: points = [[0,0],[94911151,94911150],[94911152,94911151]]
    slope of [0,0] and [94911151,94911150] != [94911151,94911150] and [94911152,94911151]
    
    we need to find GCD of (y1-y2) and (x1-x2)
    '''
    def maxPoints(self, points: List[List[int]]) -> int:
        
        ans = 0
        size = len(points)
        for x in range(size):
            slope_dict = {}
            same = 0
            for y in range(x + 1, size):
                if self.isEqual(points[x], points[y]):
                    same += 1
                else:
                    dy, dx = self.get_slope(points[x], points[y])
                    slope_dict[(dy, dx)] = slope_dict.get((dy, dx), 0) + 1
                                
            val = 0
            if len(slope_dict) > 0:
                val = max(slope_dict.values())
            ans = max(ans, val + same + 1)
            
        return ans
    
    def get_slope(self, a, b):
        dy, dx = b[1] - a[1], b[0] - a[0]
        gcd = self.gcd(dy, dx)
        return dy // gcd, dx // gcd
    
    def isEqual(self, a, b):
        return a[0] == b[0] and a[1] == b[1]

    def gcd(self, a, b):
        return a if b==0 else self.gcd(b,a % b)
