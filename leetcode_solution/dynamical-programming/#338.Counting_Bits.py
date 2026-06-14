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
        def add_one(binary_rep: list[int]) -> list[int]:
            i = len(binary_rep) - 1
            while i >= 0:
                if binary_rep[i] == 0:
                    binary_rep[i] = 1
                    return binary_rep
                else:
                    binary_rep[i] = 0
                    i -= 1
            if i == -1:
                return [1] + binary_rep

        res = []
        bit_rep = [0]
        i = 0
        while i <= n:
            res.append(sum(bit_rep))
            bit_rep = add_one(bit_rep)
            i += 1

        return res
