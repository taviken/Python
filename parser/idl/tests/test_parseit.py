from ..tools import parseit
from ..python_listener import Obj
from .expected import expected
from pathlib import Path

this_dir = Path(__file__).parent


def test_parseit():
    with open(this_dir.parent / "test_idls.idl", "r") as fd:
        data = fd.read()
    root = parseit(data)
    assert root == expected
