from .._markov import Chain, Weights

def test_weight():
    weights = Weights[str]()
    weights.add("a")
    weights + "b"
    assert weights._data == {"a":1, "b":1}
    
    weights + "a"
    assert weights._data == {"a":2, "b":1}

def test_chain():
    chain = Chain[str]()
    chain.add("a","z")
    chain.add("b", "y")
    
    expected = Weights()
    