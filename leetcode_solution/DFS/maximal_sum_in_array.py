#
#  only allow move right or down. 
#  It is a DFS problem but can be mapped to tree.
#
#
def get_maximal_sum(x, y, array):
    
    m, n = len(array[0]), len(array)
    
    if x == m-1 and y == n-1:
        return array[n-1][m-1]
    
    maximal_sum = 0
    if x < m-1:
        maximal_sum = array[y][x] + get_maximal_sum(x+1, y, array)
        
    if y < n-1:
        maximal_sum = max(maximal_sum, array[y][x] + get_maximal_sum(x, y+1, array))
    
    return maximal_sum


print get_maximal_sum(0, 0, [[2,1,4,3],[1,2,2,1],[ 4,2,1,2]])


# O(2**(m*n))
