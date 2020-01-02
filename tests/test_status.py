import collections

try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5