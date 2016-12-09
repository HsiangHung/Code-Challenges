## Q 9.5 generate all permutation of a string
##
## This problem is equivalent to find a number set [1,2,3..n]
## find all permutation
##
def permutation(s):
    import copy
    if len(s) == 1: return [s]
    
    pert_sets = {}
    
    #pert_sets[1] = [[s[0]]]
    pert_sets[1] = [[1]]
    
    n = len(s)
    i =2
    while i <= n:
        pert_sets[i] = []
        for lst in pert_sets[i-1]:
            #print (lst)
            for j in range(len(lst)+1):
                new_lst = copy.deepcopy(lst)
                new_lst.insert(j, s[i-1])
                # new_lst.insert(j, i)
                pert_sets[i].append(new_lst)
        i +=1
    
    return [''.join(x) for x in pert_sets[n]]
    
    
    
print (permutation('abcd'))