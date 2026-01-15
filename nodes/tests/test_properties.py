from ..node import *


def test_eq():
    a = Node("d")
    b = Node("d")
    assert a == b
    assert a == "d"
    assert "d" == a
    assert a is not b


def test_repr():
    a = Node("a")
    assert eval(repr(a)) == a
