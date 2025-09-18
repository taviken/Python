from typing import Dict, TypeVar, Iterable, Optional, Generic, Generator, Tuple
from collections import namedtuple


T = TypeVar("T")

ChainDict = Dict[T, int]
Probabilities = namedtuple("Probabilities", ["keys", "weights"])


class Weights(Generic[T]):
    __slots__ = ("_data",)

    def __init__(self, data: Optional[ChainDict] = None):
        _data = data if data is not None else {}
        self._data = _data

    def __add__(self, key: T) -> None:
        entry = self._data.get(key, 0) + 1
        self._data[key] = entry
        return entry

    def add(self, key: T) -> None:
        self + key

    def __iter__(self) -> Iterable[Probabilities]:
        return zip(*self._data.items())

    @property
    def probabilties(self) -> Iterable[Probabilities]:
        return iter(self)

    def __eq__(self, other: "Weights") -> bool:
        if not isinstance(other, self.__class__):
            raise ValueError("other must be of type 'Weights'")
        return self._data == other._data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._data})"


class Chain(Generic[T]):
    __slots__ = ("entries",)

    def __init__(self):
        self.entries: Dict[T, Weights] = {}

    def add(self, key: T, next_item: T) -> None:
        weights = self.entries.get(key, Weights())
        weights.add(next_item)
        self.entries[key] = weights

    def weights_by_key(self, key: T) -> Optional[Weights]:
        return self.entries.get(key)

    def __getitem__(self, key: T) -> Optional[Weights]:
        return self.weights_by_key(key)
