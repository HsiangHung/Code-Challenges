#
# 739. Daily Temperatures
#
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        stack, inspired by https://www.youtube.com/watch?v=sDKpIO2HGq0

        nums = [73,74,75,71,69,72,76,73], res = [1,1,4,2,1,1,0,0]
          index  0  1  2  3  4  5  6  7

        res = [0,0,0,0,0,0,0,0] initially

        Only inserts to stack when curr val smaller than prev:
        i  stack[-1]  curr  res stack              res
        0             73    [0]                   [0,0,0,0,0,0,0,0]
        1     73      74    [1]   (pop 0, 1-0=1)  [1,0,0,0,0,0,0,0]
        2     74  <   75    [2]   (pop 1, 2-1=1)  [1,1,0,0,0,0,0,0]
        3     75  >   71    [2,3]                 [1,1,0,0,0,0,0,0]
        4     71  >   69    [2,3,4]               [1,1,0,0,0,0,0,0]
        5     69  <   72    [2,3] + [5] (pop 4, 5-4=1)  [1,1,0,0,1,0,0,0]
              71  <   72    [2] + [5] (pop 3, 5-3=2)  [1,1,0,2,1,0,0,0]
                            
                            [2,5]                     [1,1,0,2,1,0,0,0]

        6     72  >   76    [2] + [6] (pop 5, 6-5=1)  [1,1,0,2,1,1,0,0]
              72  >   76    [] + [6] (pop 2, 6-4=4)  [1,1,4,2,1,1,0,0]
        7     76  >   73    [6] + [7]                [1,1,4,2,1,1,0,0]

        final res: [1,1,4,2,1,1,0,0]
        """
        n = len(temperatures)
        res = [0] * n

        stack = [0] # 0: index = 0, 0-th element
        for i in range(1, n):

            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                wait_time = i - idx
                res[idx] = wait_time
            
            stack.append(i)
        
        return res
