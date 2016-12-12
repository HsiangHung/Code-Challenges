## Q9.8: Dynamic Programming Python implementation of Coin Change problem
#
def numWays(coin, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    dp = [[0 for x in range(m)] for x in range(n+1)]
    
    #print (dp)
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        dp[0][i] = 1

    #print (dp)

    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including coin[j]
            x =0
            if i-coin[j] >= 0: x = dp[i - coin[j]][j]
 
            # Count of solutions excluding coin[j]
            y =0
            if j >= 1: y = dp[i][j-1]
 
            # total count
            dp[i][j] = x + y
        
            print (i, coin[j], x,y)
 
    return dp[n][m-1]



coins = [1,5,10,25]
print (numWays(coins, len(coins), 26))