## Q9.4: generate all possible subsets from a set
## e.g. {1,2,3} -> {{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
#
def get_subset(s):
    dp = {1: [set({x}) for x in s]}
    print (dp)
    
    subset_len = 2
    while subset_len <= len(s):
        dp[subset_len] = []
        for x in dp[subset_len-1]:
            for y in s:
                subset = list(x)
                subset.append(y)
                subset = set(subset)
                if subset not in dp[subset_len]: 
                    dp[subset_len].append(subset)
        
        subset_len += 1
        
    return dp[len(s)]
    
    
print (get_subset({1,2,3,4}))

