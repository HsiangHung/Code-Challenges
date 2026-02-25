class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        idea: n = (n-1) + 1 
        we can direct sum on binary digits, and if 1+1=2 -> move to next decimal
        e.g.
        5 = 101, 
        6 = 5 + 1 = 101 + 1 -> 102 -> 110 
        7 = 6 + 1 = 110 + 1 -> 111
        8 = 7 + 1 = 111 + 1 -> 112 -> 120 -> 200 -> 1000
        """
        dp = [[0], [1]]
        x = 2
        while x <= n:
            arr = dp[x-1].copy()
            arr[-1] += 1

            y = 1
            while y < len(arr) and arr[len(arr)-y] == 2:
                arr[len(arr)-y] = 0
                y += 1
                arr[len(arr)-y] += 1
            
            if arr[0] == 2:
                arr[0] = 0
                dp.append([1] + arr)
            else:
                dp.append(arr)
            x += 1

        return [sum(x) for x in dp[:(n+1)]]

