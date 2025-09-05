from operator import add, sub, mul, truediv


class Percent:
    __slots__ = ("_value",)

    def __init__(self, value: float = 0.0):
        self.value: float = value

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, new_value: float) -> None:
        if not isinstance(new_value, float):
            raise ValueError(f"new_value must be of type float, got '{type(new_value)}")
        self._assert_bounds(new_value)
        self._value = new_value

    @staticmethod
    def _assert_bounds(value):
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"new_value must be between 0.0 and 1.0, got '{value}'")

    def __repr__(self) -> str:
        return f"Percent(value={self._value})"

    def __str__(self) -> str:
        return f"{self._value *100.0} %"

    def __operate__(self, other, oper):
        self._assert_bounds(other)
        return oper(other, self._value)

    def __add__(self, other: float) -> float:
        return self.__operate__(other, add)

    def __sub__(self, other: float) -> float:
        return self.__operate__(other, sub)

    def __truediv__(self, other: float) -> float:
        return self.__operate__(other, truediv)

    def __mul__(self, other: float) -> float:
        return self.__operate__(other, mul)
