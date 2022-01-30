from typing import List, Any

import numpy as np
import random
from numpy import ndarray

N = 1000
n = 100


class Node:
    def __init__(self):
        self.num = -1  # int
        self.right_child = -1  # int
        self.left_child = -1  # int
        self.parent = -1  # int

    def __str__(self):
        return str(self.num) + "[" + str(self.left_child) + ", " + str(self.right_child) + "]"


# tree = np.empty(2 * N + 1, dtype=Node)
tree1 = [Node() for i in range(2 * N + 1)]
tree2 = [Node() for i in range(2 * N + 1)]


def change_leaves(tree, a, b):
    parenta = tree[a].parent
    parentb = tree[b].parent

    if tree[parenta].right_child == a:
        tree[parenta].right_child = b
    else:
        tree[parenta].left_child = b
    tree[a].parent = parentb
    if tree[parentb].right_child == b:
        tree[parentb].right_child = a
    else:
        tree[parentb].left_child = a
    tree[b].parent = parenta


def growing_tree(tree, n):
    tree[0].left_child = 1
    tree[0].right_child = 2
    tree[0].num = 1
    tree[1].parent = tree[2].parent = 0
    tree[1].right_child = tree[1].left_child = -1
    tree[2].right_child = tree[2].left_child = -1

    for i in range(2, n + 1):
        number = random.randint(0, i)
        # print(i - 1, number + i - 1)
        change_leaves(tree, i - 1, number + i - 1)
        tree[i - 1].right_child = 2 * i - 1
        tree[i - 1].left_child = 2 * i
        tree[i - 1].num = i
        tree[2 * i - 1].parent = i - 1
        tree[2 * i].parent = i - 1
        tree[2 * i - 1].right_child = -1
        tree[2 * i - 1].left_child = -1
        tree[2 * i].right_child = -1
        tree[2 * i].left_child = -1


def gen_list_tree(n):
    return [i - 1 for i in range(2, n + 1)]


def growing_tree_list(tree, n, l):
    tree[0].left_child = 1
    tree[0].right_child = 2
    tree[0].num = 1
    tree[1].parent = tree[2].parent = 0
    tree[1].right_child = tree[1].left_child = -1
    tree[2].right_child = tree[2].left_child = -1

    for i in range(2, n + 1):
        number = l[i - 2]
        # print(i - 1, number + i - 1)
        change_leaves(tree, i - 1, number + i - 1)
        tree[i - 1].right_child = 2 * i - 1
        tree[i - 1].left_child = 2 * i
        tree[i - 1].num = i
        tree[2 * i - 1].parent = i - 1
        tree[2 * i].parent = i - 1
        tree[2 * i - 1].right_child = -1
        tree[2 * i - 1].left_child = -1
        tree[2 * i].right_child = -1
        tree[2 * i].left_child = -1


l = gen_list_tree(2)
growing_tree_list(tree1, 2, l)
growing_tree(tree2, 2)

for i in range(4 * 2):
    print(tree1[i])


# print(tree[1])

def phi(tree):
    def phi_aux(tree, i):
        if tree[i].left_child == -1 and tree[i].right_child == -1:
            return ""
        return "(" + phi_aux(tree, tree[i].left_child) + ")" + phi_aux(tree, tree[i].right_child)

    return phi_aux(tree, 0)


def equals(a1, a2):
    return phi(a1) == phi(a2)


print("t1 = t2 ? ", equals(tree1, tree2))


def gen_all_list(n):
    return gen_aux(n, 2, [[]])


def gen_aux(n, k, res):
    res2 = []
    for e in res:
        for i in range(0, k):
            res2.append(e + [i])
    if (k == n):
        return res2
    return gen_aux(n, k + 1, res2)


def couverture(n):
    lists = gen_all_list(n)
    trees = dict()

    for listTemp in lists:
        tree = [Node() for _ in range(2 * N + 1)]
        growing_tree_list(tree, n, listTemp)
        s = phi(tree)
        if s in trees:
            trees[s] += 1
        else:
            trees[s] = 1
    return trees


# print(couverture(3)) #Max
class AB :
    def __init__(self, tag,  *, father = None, right = None, left = None) :
        self.father = father
        self.right = right
        self.left = left
        self.tag = tag

    def isLeaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        if self.isLeaf():
            return ""
        else:
            return "(" + str(self.left) + ")" + str(self.right)


def algoRemy(n):
    nb_intern_node = 0
    arbre = AB(1)
    all_nodes = [arbre]

    while nb_intern_node < n:
        r = random.randint(0, len(all_nodes)-1)
        f = all_nodes[r]
        pile_face = random.randint(0, 1)
        nouveau = AB(0)
        all_nodes.append(nouveau)
        if pile_face == 0:
            f.left = nouveau
            nouveau.father = f
        else :
            f.right = nouveau
            nouveau.father = f
        nb_intern_node += 1
    return all_nodes


print(algoRemy(4)[0])
