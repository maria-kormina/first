import pytest


def get_list(start, stop):
    pass

def test_list():
    assert get_list(1,3) == [1,2,3]
    assert get_list(10,3) == []
    assert get_list(9,9) == [9]
