#
#  given an array for each item's weight and number of days needed to finish, 
#  find min capacity of truck (in a day, truck can ship multiple items)
#  the shipping need to be in order
#   
#  e.g. w = [1,2,3,2], 
#  * if day = 1, [1,2,3,2] => min_cap = 8
#  * if day = 4, [1][2][3][2] => min_cap 3
#  * if day = 2, we have [1,2][3,2] or [1][2,3,2], or [1,2,3][2] => min_cap = 5
#  * if day = 3, [1,2][3][2] or [1][2,3][2] => min_cap = 3
#
def get_min_capactity(day, w):
    if day == 1: return sum(w)
    if len(w) == day: return max(w)

    min_capacity = sum(w)

    i = 0
    while i <= len(w) - day:
        capacity = sum(w[:i+1])
        min_capacity = min(min_capacity, max(capacity, get_min_capactity(day-1, w[i+1:])))
        i += 1

    return min_capacity


w = [1,2,3,2]
day = 2
print (get_min_capactity(day, w))

    
