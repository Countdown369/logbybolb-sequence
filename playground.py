def logbybolb(n, length):
    master = []
    master.append(n)
    for i in range(length-1):
        master.append(actor(n, master))
        
    return master
        
            
def actor(minimum, master):
    if minimum not in master[-minimum:]:
        return minimum
    else:
        return actor(minimum+1, master)


def repeatingstart(lst):
    for i in range(1, (len(lst) // 2)+1):
        if lst[0:i] == lst[i:2*i]:
            return i
    return -1

def repeating(lst):
    #import pdb; pdb.set_trace()
    indices = [i for i in range(len(lst)) if lst[i] == max(lst)]
    if indices[-1] - indices[-2] == indices[-2] - indices[-3]:
        return {"length": indices[-1] - indices[-2]}
    else:
        diffs = [j-i for i, j in zip(indices[:-1], indices[1:])]
        if repeatingstart(diffs) != -1:
            return {"length": len(lst[0:repeatingstart(lst)])}
        else:
            return -1
