import pytest
from pytest import list_of, nonempty_list_of, dict_of, Generator

import exo3
import exo2_1
from ternary_trie import fusion


@pytest.mark.randomize(l=list_of(int, min_items=1, max_items=10), min_num=0, ncalls=10)
def test_list_is_min_heap(l):
    assert exo3.prop_is_min_heap(l)


@pytest.mark.randomize(l=list_of(int, min_items=1), min_num=0, ncalls=100)
def test_insert_heap(l):
    res = []
    for i in l:
        res = exo3.insert(res, i)
    assert exo3.prop_is_min_heap(res)


@pytest.mark.randomize(v=int, min_num=0, ncalls=10)
def test_create_one(v):
    res = [v]
    assert exo3.prop_is_min_heap(res)


@pytest.mark.randomize(ncalls=100)
def test_extract_min():
    res = []
    for i in range(10):
        res = exo3.insert(res, i)
    for i in range(10):
        assert exo3.extract_min(res) == i
        assert exo3.prop_is_min_heap(res)


@pytest.mark.randomize(l=list_of(int, min_items=1, max_items=50), min_num=0, max_num=50, ncalls=1000)
def test_extract_min(l):
    res = []
    for i in range(len(l)):
        res = exo3.insert(res, l[i])
    temp = res[1:]
    assert len(temp) == len(res) - 1
    exo3.extract_min(res)
    assert exo3.prop_is_min_heap(res)
    for e in temp:
        assert e in res


# 3.15
@pytest.mark.randomize(liste1=list_of(str, min_items=1, max_items=10), liste2=list_of(str, min_items=1, max_items=10), min_num=0, max_num=50, ncalls=1)
def test_ternary_tree(liste1, liste2):
    abr = exo2_1.find_words(exo3.fusion_exo3(liste1, liste2))
    for e in liste1:
        assert e in abr
    for e in liste2:
        assert e in abr
    assert exo2_1.is_sorted(abr)
