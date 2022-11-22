import pytest


def get_numerated(l: list):
    pass


def test_():
    assert get_numerated(['b','c']) == [(0,'b'),(1,'c')]
    assert get_numerated('PyThOn') == [
        (0,'P'),
        (1,'y'),
        (2,'T'),
        (3,'h'),
        (4,'O'),
        (5,'n'),
    ]
