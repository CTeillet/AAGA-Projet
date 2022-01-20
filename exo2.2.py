from typing import List, Any

import numpy as np
import random
from numpy import ndarray

N = 1000
n = 100


class Node:
    def __init__(self):
        self.num = None  # int
        self.right_child = None  # int
        self.left_child = None  # int
        self.parent = None  # int


# tree = np.empty(2 * N + 1, dtype=Node)
tree = [Node() for i in range(2 * N + 1)]


def change_leaves(a, b):
    parenta = tree[a].parent
    parentb = tree[b].parent

    if tree[parenta].right_child == a:
        tree[parenta].right_child = b
    else:
        tree[parenta].left_child = b
    tree[a].parent = parentb
    if  tree[parentb].right_child == b:
        tree[parentb].right_child = a
    else:
        tree[parentb].left_child = a
    tree[b].parent = parenta


def growing_tree(n):
    tree[0].left_child = 1
    tree[0].right_child = 2
    tree[0].num = 1
    tree[1].parent = tree[2].parent = 0
    tree[1].right_child = tree[1].left_child = -1
    tree[2].right_child = tree[2].left_child = -1

    for i in range(2, n + 1):
        number = random.randint(0, i)
        print(i - 1, number + i - 1)
        change_leaves(i - 1, number + i - 1)
        tree[i - 1].right_child = 2 * i - 1
        tree[i - 1].left_child = 2 * i
        tree[i - 1].num = i
        tree[2 * i - 1].parent = i-1
        tree[2 * i].parent = i - 1
        tree[2 * i - 1].right_child = -1
        tree[2 * i - 1].left_child = -1
        tree[2 * i].right_child = -1
        tree[2 * i].left_child = -1


growing_tree(n)
print(tree)
