from biokit import Taxonomy
import pytest
import os


def test_taxonomy():
    t = Taxonomy()
    t.load_records()
    lineage = t.get_lineage(9606)


    assert t.fetch_by_id('10090')['name'] == 'Mus musculus' 

    ret = t.fetch_by_name('Mus Musculus')
    assert ret[0]['id'] == '10090'

    lineage = t.get_lineage_and_rank(9606)

    tree = t.get_family_tree(9606)


