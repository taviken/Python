from ..node import *
import pytest


@pytest.fixture
def setup1():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")

    a.add_right(b)
    a.add_right(c)
    b.add_right(d)
    b.add_right(e)
    c.add_right(f)
    c.add_right(g)
    return a, b, c, d, e, f, g


@pytest.fixture
def setup2():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d1 = Node("d")
    d2 = Node("d")
    a.add_right(b)
    a.add_right(c)
    b.add_right(d1)
    c.add_right(d2)
    return a, b, c, d1, d2


def test_level_order(setup1):
    a, b, c, d, e, f, g = setup1
    assert tuple(a.level_order_traversal()) == ("a", "b", "c", "d", "e", "f", "g")
    assert tuple(a.level_order_traversal(as_value=False)) == (a, b, c, d, e, f, g)


def test_pre_order(setup1):
    a, b, c, d, e, f, g = setup1
    assert tuple(a.pre_order_traversal()) == ("a", "b", "d", "e", "c", "f", "g")
    assert tuple(a.pre_order_traversal(as_value=False)) == (a, b, d, e, c, f, g)


def test_post_order(setup1):
    a, b, c, d, e, f, g = setup1
    assert tuple(a.post_order_traversal()) == ("d", "e", "b", "f", "g", "c", "a")
    assert tuple(a.post_order_traversal(as_value=False)) == (d, e, b, f, g, c, a)


def test_find_greedy(setup2):
    a, b, c, d1, d2 = setup2
    expected = tuple(map(id, a.find_greedy("d", as_value=False)))
    assert expected == (id(d1), id(d2))
    assert not bool(tuple(a.find_greedy("foo")))


def test_find_lazy(setup2):
    a, *_, d1, _ = setup2
    res = a.find_lazy("d", as_value=False)

    assert id(res) == id(d1)
    assert a.find_lazy("foo") is None
