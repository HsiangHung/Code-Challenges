#  91. Decode Ways (medium)
#  https://leetcode.com/problems/decode-ways/
# 
#
class Solution:
     def numDecodings(self, s: str) -> int:
          '''
          This problem is unable to use DFS, for testing case like 
          s = "111111111111111111111111111111111111111111111", time exceeds.          
          We need to use dynamical programming. Return the last dp.
          e.g. s = "2225":
               dp[0] = dp[1] = 1 
               "22":   dp[2] = (dp[1] + "2") & (dp[0] + "22") = 1 + 1 = 2
               "222":  dp[3] = (dp[2] + "2") & (dp[1] + "22") = 2 + 1 = 3
               "2225": dp[4] = (dp[3] + "5") & (dp[2] + "25") = 3 + 2 = 5
               
          e.g. s = "2265":
               dp[0] = dp[1] = 1 
               "22":   dp[2] = (dp[1] + "2") & (dp[0] + "22") = 1 + 1 = 2
               "226":  dp[3] = (dp[2] + "6") & (dp[1] + "26") = 2 + 1 = 3
               "2265": dp[4] = (dp[3] + "5") & (dp[2] + "65") = 3 + 0 = 3

          e.g. s = "2205":
               dp[0] = dp[1] = 1 
               "22":   dp[2] = (dp[1] + "2") & (dp[0] + "22") = 1 + 1 = 2
               "220":  dp[3] = (dp[2] + "0") & (dp[1] + "20") = 0 + 1 = 1
               "2205": dp[4] = (dp[3] + "5") & (dp[2] + "05") = 1 + 0 = 1
               
          e.g. s= "0225"; return 0 since no "0" and no "02"
          '''
          if s[0] == "0": return 0
          
          dp = {0: 1, 1: 1}
          i = 2
          while i <= len(s):
               dp[i] = 0
               if s[i-2: i] <= "26" and s[i-2] != "0": # consider s[i-2] = "1", s[i-1] = "0", then "10" is valid
                    dp[i] = dp[i-2]
               if s[i-1] != "0": # add curr s[i]
                    dp[i] += dp[i-1]
               i += 1
          
          return dp[len(s)]
    

     def dp_list_all_decodes(self, s: str):
          """
          This version lists all decoding ways, and hits memory limitation.
          But code is clear.
          """

          alpha_map = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E", 
                         "6": "F", "7": "G", "8": "H", "9": "I", "10": "J", 
                         "11": "K", "12": "L", "13": "M", "14": "N", "15": "O", "16": "P", "17": "Q", "18": "R", "19": "S", "20": "T",
                         "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y",
                         "26": "Z"}

          dp = {0: [[s[0]]]}
          for i in range(1, len(s)):
               prev = dp[i-1]

               curr = []
               for j in prev:

                    if s[i] != "0":
                         curr.append( j + [s[i]])

                    if len(j[-1]) < 2 and (j[-1] + s[i] in alpha_map):
                         curr.append(j[:-1] + [j[-1] + s[i]])

               dp[i] = curr

          return len(dp[len(s)-1])
