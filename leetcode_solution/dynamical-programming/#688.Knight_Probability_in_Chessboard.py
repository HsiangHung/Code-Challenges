#  688. Knight Probability in Chessboard (medium)
#  https://leetcode.com/problems/knight-probability-in-chessboard/
#
class Solution:
    '''
    https://blog.csdn.net/fuxuemingzhu/article/details/82747623
    
    Use dynamical programming, turn O(8^K) to O(K*N^2)
    '''
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0: return 1
        
        dp = self.get_zeroDP(N)
                
        for x2, y2 in self.move(c, r):
            if 0 <= x2 < N and 0 <= y2 < N: dp[y2][x2] = 1
        
        i = 2
        while i <= K:            
            dp2 = self.get_zeroDP(N)
            
            for y in range(N):
                for x in range(N):
                    for x2, y2 in self.move(x, y):
                        if 0 <= x2 < N and 0 <= y2 < N:
                            dp2[y][x] += dp[y2][x2] 
            
            dp = dp2.copy()
            i += 1
        
        num_ins = 0
        for y in range(N):
            num_ins += sum([dp[y][x] for x in range(N)])
        
        return num_ins/8**K
            
    def get_zeroDP(self, N):
        dp = []
        for _ in range(N):
            dp.append([0]*N)
        return dp
    
    def move(self, x, y):
        return [(x+dx, y+dy) for dx, dy in [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]]
        
        