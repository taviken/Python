from peg_parser import Node
import pytest


def test_node():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.add_left(c)
    a.add_right(b)
    b.add_left(d)
    b.add_right(e)
    expected = None
    assert a == expected
