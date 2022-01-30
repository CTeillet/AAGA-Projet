import ternary_trie


def getLeftChild(i):
    j = 2 * i + 1
    return j


def getRightChild(i):
    return getLeftChild(i) + 1


def getFather(i):
    f = (i - 1) // 2
    return f


def insert(bh, v):
    i = len(bh)
    bh.append(v)
    f = getFather(i)
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

    if right < len(bh) and bh[right] < bh[curr]:
        curr = right

    if curr != i:
        tmp = bh[i]
        bh[i] = bh[curr]
        bh[curr] = tmp
        min_heapify(bh, curr)


def prop_is_min_heap(bh):
    for i in range(1, len(bh)):
        if bh[getFather(i)] > bh[i]:
            return False
    return True


def gen_arbre_tern_liste_exo3(liste):
    arbre = ternary_trie.gener_feuille()
    for word in liste:
        arbre = ternary_trie.insert(arbre, word)
    return arbre


def fusion_exo3(liste1, liste2):
    arbre1 = gen_arbre_tern_liste_exo3(liste1)
    arbre2 = gen_arbre_tern_liste_exo3(liste2)
    return ternary_trie.fusion(arbre1, arbre2)