from .._normal import NormalArray


def test_normal():
    cats = ["w", "u", "b", "r", "g"]
    n = NormalArray(cats)
    assert n
    n.inc("w")
    assert n.w == 1

    n.reset()
    for cat in cats:
        n.inc(cat)
    assert n.normalized == {"w": 0.2, "u": 0.2, "b": 0.2, "r": 0.2, "g": 0.2}
