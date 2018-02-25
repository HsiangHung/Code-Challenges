## Q9.6: generating a set of combined parentheses
## e.g. n=2, {'(())', '()()'}
## e.g. n=3, {'((()))', '(())()', '()(())', '(()())', '()()()'}
##
## idea: to look for left parentheses: "(" and inert an "()" at the
##       beginning and behind the left parentheses
##
def parathese(n):
    dp = {1: ["()"]}
    pa = 2
    while pa <= n:
        subset = set({})
        for x in dp[pa-1]:
            print (x)
            left_par_index = [i for i in range(len(x)) if x[i] == "("]
            subset.add("()"+x)
            for i in left_par_index:
                new_string = x[:i+1]+"()"+x[i+1:]
                subset.add(new_string)
            
        print (subset)
        dp[pa] = subset
        pa += 1
        
    return dp[n]
    
print (parathese(3))