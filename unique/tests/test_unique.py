"""Unique meta class tester"""
import pytest
from unique import make_unique, UniqueValueError


def test_make_unique():
    """Tests that unique metaclass disallows more than one key value"""
    class Test(metaclass=make_unique(key='name')):
        """Test class"""
        name: str

        def __init__(self, name):
            self.name = name

    _ = Test('bar')
    with pytest.raises(UniqueValueError):
        _ = Test('bar')
