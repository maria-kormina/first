import pytest


def get_slices(list_, element):
    pass


def test_():
    l = [1, 2, 3, 4, 5]
    assert get_slices(l, 3) == [1, 2], [3, 4, 5]
    assert get_slices(l, '3') == [1, 2, 3, 4, 5]
