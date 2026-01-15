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


def test_eq():
    a = Node("d")
    b = Node("d")
    assert a == b
    assert a == "d"
    assert "d" == a
    assert a is not b


def test_tree_prop(setup1):
    a, b, c, _, e, _, g = setup1
    g.add_right("h")
    assert a.is_root
    assert not b.is_root
    assert c.is_binary
    assert e.is_leaf
    assert g.is_single_link


def test_repr():
    a = Node("a")
    assert eval(repr(a)) == a


def test_as_dict(setup1):
    a, *_ = setup1
    assert a.as_dict == {
        "value": "a",
        "children": [
            {"value": "b", "children": [{"value": "d"}, {"value": "e"}]},
            {"value": "c", "children": [{"value": "f"}, {"value": "g"}]},
        ],
    }


def test_format(setup1):
    a, *_ = setup1
    assert (
        format(a, "pipe")
        == "└── a\n    ├── b\n    │   ├── d\n    │   └── e\n    └── c\n        ├── f\n        └── g\n"
    )
    assert (
        f"{a:dict}"
        == "{'children': [{'children': [{'value': 'd'}, {'value': 'e'}], 'value': 'b'},\n              {'children': [{'value': 'f'}, {'value': 'g'}], 'value': 'c'}],\n 'value': 'a'}\n"
    )
