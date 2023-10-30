from shapes import Point3

foo = Point3(1, 2, 3)
bar = Point3(4, 5, 6)


def test_point3():
    a = foo+bar
    expected = Point3(5, 7, 9)
    assert a == expected, f"Expected {expected}, got {a}"
