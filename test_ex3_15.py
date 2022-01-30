import pytest
from pytest import list_of, nonempty_list_of, dict_of, Generator

import exo2_1

@pytest.mark.randomize(liste1=list_of(str, min_items=1, max_items=10), liste2=list_of(str, min_items=1, max_items=10), min_num=0, max_num=50, ncalls=1)
def test_ternary_tree(liste1, liste2):
    abr = exo2_1.find_words(exo3.fusion_exo3(liste1, liste2))
    for e in liste1:
        assert e in abr
    for e in liste2:
        assert e in abr
    assert exo2_1.is_sorted(abr)