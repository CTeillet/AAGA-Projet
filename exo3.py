import pytest
from pytest import list_of, nonempty_list_of, dict_of, Generator


def getLeftChild(i):
    j = 2 * i
    if i == 0:
        j = 1
    return j


def getRightChild(i):
    return getLeftChild(i) + 1


def getFather(i):
    f = (i - 1) // 2
    return f


# TODO : probleme f pas initialisé
def insert(bh, v):
    i = len(bh)
    bh.append(v)
    f = 0
    while i > 0 and bh[i] < bh[f]:
        tmp = bh[i]
        bh[i] = bh[f]
        bh[f] = tmp
        i = f
        f = getFather(i)
    return bh


def extract_min(bh):
    res = bh[0]
    bh[0] = bh[-1]
    bh.pop()
    min_heapify(bh, 0)
    return res


def min_heapify(bh, i):
    left = getLeftChild(i)
    right = getRightChild(i)
    curr = i

    if left < len(bh) and bh[left] < bh[curr]:
        curr = left

    if right <= len(bh) and bh[right] < bh[curr]:
        curr = right

    if curr != i:
        tmp = bh[i]
        tmp[i] = bh[curr]
        bh[curr] = tmp
        min_heapify(bh, curr)


def prop_is_min_heap(bh):
    for i in range(1, len(bh)):
        if bh[getFather(i)] < bh[i]:
            return False
    return True


@pytest.mark.randomize(l=list_of(int, min_items=1, max_items=10), min_num=0, ncalls=10)
def test_list_is_min_heap(l):
    assert prop_is_min_heap(l)