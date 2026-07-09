#
#  2831. Find the Longest Equal Subarray
#
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        """
        ref: https://www.youtube.com/watch?v=viTxUBa_Jdo
        going through index for each number built in a dict
        using two points, to look up longest possible sequence
        """

        def get_longest_sequence(arr, k):
            """
            arr is index array. contignuous index
            * e.g. if we have arr=[0,1,4,5]
              if k=1, return 2
              if k=2, return 4
            * e.g. if we have arr=[0,1,4,5,7,8,9,10,12,13,14]
              if k=2, return 7
              if k=3, return 9
              if k=4, return 14
            """

            i = 0
            max_len = 0
            for j in range(len(arr)):
                # shrink from the left until this window is affordable
                while (arr[j] - arr[i]) - (j - i) > k:
                    i += 1
                max_len = max(max_len, j - i + 1)
            return max_len

  


        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = num_dict.get(nums[i], []) + [i]
        
        # e.g. nums = [1,1,2,2,1,1], {1:[0,1,4,5],2:[2,3]}
        #      nums = [1,1,2,2,1,1,1,2,1,1,1,1], {1:[0,1,4,5,6,8,9,10,11,12,13], 2: [2,3,7]}
        

        longest_seq = 1
        for num in num_dict:
            seq = get_longest_sequence(num_dict[num], k)
            longest_seq = max(longest_seq, seq)
        
        return longest_seq