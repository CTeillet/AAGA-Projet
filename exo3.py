


def getLeftChild(i) :
    j = 2*i
    if i == 0:
        j = 1
    return j

def getRightChild(i):
    return getLeftChild(i) + 1

def getFather(i) : 
    f = (i-1) // 2


def insert(bh, v) :
    i = len(bh)
    bh.append(v)
    while i > 0 and bh[i] < bh[f] :
        tmp = bh[i]
        bh[i] = bh[f]
        bh[f] = tmp
        i = f
        f = getFather(i)
    return bh

def extract_min(bh) :
    res = bh[0]
    bh[0] = bh[-1]
    bh.pop()
    min_heapify(bh, 0)


def min_heapify(bh, i):
    left = getLeftChild(i)
    right = getRightChild(i)
    curr = i
    
    if left < len(bh) and bh[left] < bh[curr] :
        curr = left

    if right <= len(bh) and bh[right] < bh[curr] :
        curr = right
    
    if curr != i :
        tmp = bh[i]
        tmp[i] = bh[curr]
        bh[curr] = tmp
        min_heapify(bh, curr)

def prop_is_min_heap(bh) : 
    for i in range(1, len(bh)) :
        if bh[getFather(i)] < bh[i] :
            return False
    return True 



    





