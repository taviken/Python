from .._percent import Percent
import pytest


def test_percent():
    p = Percent()
    assert p.value == 0.0
    p.value = 0.2
    assert p.value == 0.2


def test_out_of_bounds():
    p = Percent()

    with pytest.raises(ValueError):
        p.value = 1.2

    with pytest.raises(ValueError):
        p.value = -1.2

    with pytest.raises(ValueError):
        p + 1.2

    with pytest.raises(ValueError):
        p += 1.2

    with pytest.raises(ValueError):
        p - 4.0
