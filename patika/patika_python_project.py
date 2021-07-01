# Ömer Faruk BAYSAL -- Patika Python Project

#%% Part 1

def flatten(inp):
    """
    Recursive flatten function
    """
    out=[]

    for i in inp:
        if type(i)==list:
            [out.append(j) for j in flatten(i)]
        else:
            out.append(i)
    
    return out;


inp= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print("Output of Part 1:",flatten(inp))


#%% Part 2

def listReverser(l):
    """
    Recursive list reversing function
    """

    if type(l)!=list:
        return None

    l.reverse()

    for i in l:
        listReverser(i)


inp=[[1, 2], [3, 4], [5, 6, 7]]
listReverser(inp)

print("Output of Part 2:",inp)
# %%
