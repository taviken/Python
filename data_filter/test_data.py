from .data import data, get_intervals, ID, modes


def test_interval():

    filtered = list(filter(lambda x: x[ID] in {i.value for i in modes}, data))

    res = get_intervals(filtered)
    assert res is None
