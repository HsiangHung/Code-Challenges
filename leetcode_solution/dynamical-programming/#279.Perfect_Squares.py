class Solution:
    def numSquares(self, n: int) -> int:
        
        self.min_squares = {} # need to save this, otherwise time limitation
        def DFS(num):
            if num in self.min_squares:
                return self.min_squares[num] # no need to run DFS if num has sum of squares

            if num == 1:
                return [1]

            sqrt_n = int(sqrt(num))
            if sqrt_n ** 2 == num:
                return [num]

            i = sqrt_n
            min_num_squares = None
            while i >= 1:
                if i**2 <= num-i**2: # num = m^2 + n^2 and both m^2 < n^2
                    squares = [i**2] + DFS(num-i**2)
                    if min_num_squares is None or len(squares) < len(min_num_squares):
                        min_num_squares = squares
                        self.min_squares[num] = squares
                i -= 1
                
            return min_num_squares

        # print(DFS(n))

        return len(DFS(n))


        