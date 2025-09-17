from typing import Dict, TypeVar, Iterable, Optional, Generic, Generator, Tuple

T = TypeVar("T")

ChainDict= Dict[T, int]

class Weights(Generic[T]):
    __slots__=("_data",)
    
    def __init__(self, data:Optional[ChainDict]=None):
        _data = data if data is not None else {}
        self._data = _data
    
    def __add__(self, key:T)->None:
        entry = self._data.get(key, 0)
        entry += 1
        self._data[key] = entry
        return entry

    def add(self, key:T)->None:
        self + key
    
    @property
    def probabilties(self)->Generator[Tuple[T],Tuple[int]]:
        return zip(*self._data)
    
    def __eq__(self, other:"Weights")->bool:
        if not isinstance(other, self.__class__):
            raise ValueError("other must be of type 'Weights'")
        return self._data == other._data
    
class Chain(Generic[T]):
    __slots__ = ("entries",)
    def __init__(self):
        self.entries: Dict[T, Weights] = {}
    
    def add(self, key:T, next_item:T)->None:
        weights = self.entries.get(key, Weights())
        self.entries[key] = weigthts + next_item
    
    def weights_by_key(self, key:T)->Optional[Weights]:
        return self.entries.get(key)
    
    def __getitem__(self, key:T)->Optional[Weights]:
        return self.weights_by_key(key)
    
    
        
    
    
    
    