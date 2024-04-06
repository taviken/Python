import numpy as np
from dataclasses import dataclass


@dataclass
class Point:
    _arr = None

    @classmethod
    def _as_arr(cls, other):
        return cls(*other)

    def _cast(self, other):
        return other if isinstance(other, self.__class__) else self._as_arr(other)

    def __add__(self, other):
        return self._as_arr(self._arr + self._cast(other).arr)


class Point3(Point):
    x: float
    y: float
    z: float

    def __init__(self, x: float = 0,
                 y: float = 0,
                 z: float = 0):
        self.x = x
        self.y = y
        self.z = z
        self._arr = np.array((x, y, z), dtype=np.float32)
