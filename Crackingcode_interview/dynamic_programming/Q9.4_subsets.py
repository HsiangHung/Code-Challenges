### Q9.4: generate all possible subsets from a set
#
def getSubsets(a):
    import copy
    
    subset = {}
    subset[1] = []
    for ch in a:
        subset[1].append(set({ch}))
    if len(a) == 1: return subset
    
    m = 2
    while m <= len(a):
        subset[m] = []
        for ch in subset[m-1]:
            #print (ch)
            for i in a:
                #print (i)
                new_ch = copy.deepcopy(ch)
                new_ch.add(i)
                if new_ch not in subset[m] and len(new_ch) == m: subset[m].append(new_ch)
        m +=1
    return subset
    
print (getSubsets({1,2,3,4}))    