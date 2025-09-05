from typing import List, Tuple, Dict, Union
import pandas as pd

Categories = Union[List[str] | Tuple[str]]


class NormalArray:
    def __init__(self, categories: Categories) -> None:
        self.categories = categories
        self.reset()

    def inc(self, category: str, value: int = 1) -> None:
        if category not in self.categories:
            raise ValueError(
                f"{category} not a valid category. Valid options are: {self.categories}"
            )
        _val = getattr(self, category)
        setattr(self, category, _val + value)

    @property
    def normalized(self) -> Dict[str, float]:
        data = (getattr(self, x) for x in self.categories)
        denom = sum(data)
        out = {cat: getattr(self, cat) / denom for cat in self.categories}
        return out

    def reset(self):
        data = {cat: 0 for cat in self.categories}
        self.__dict__.update(data)
