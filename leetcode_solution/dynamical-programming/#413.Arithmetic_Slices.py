# [#413] Arithmetic Slices
#
#
#
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2: return 0
        
        # store indices of subsequences
        
        dp = {3: [(i, i+2) for i in range(len(A)-2) if A[i+1]-A[i]==A[i+2]-A[i+1]]}
        
        seq_len = 4
        while seq_len <= len(A):
            
            dp[seq_len] = []
            for seq in dp[seq_len-1]:
                if seq[1] != len(A)-1 and A[seq[1]+1]-A[seq[1]] == A[seq[1]]-A[seq[1]-1]:
                    dp[seq_len].append((seq[0], seq[1]+1))
   
            seq_len += 1
    
        return sum([len(dp[seq_len]) for seq_len in dp])