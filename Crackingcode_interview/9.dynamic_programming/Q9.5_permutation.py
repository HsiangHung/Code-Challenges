## Q 9.5 generate all permutation of a string
##
## This problem is equivalent to find a number set [1,2,3..n]
## find all permutation
##
def permutation(s):
	dp = {1: [[1]]}
    sub_len = 2
    while sub_len <= m:
        dp[sub_len] = []
        for sub in dp[sub_len-1]:
            for y in range(sub_len+1):
                new_list = [x for x in sub]
                new_list.insert(y, sub_len)
                if new_list not in dp[sub_len]:
                    dp[sub_len].append(new_list)
                
        sub_len += 1
    
    return len(dp[m])
    
    
    
print (permutation(4))