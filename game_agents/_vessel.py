from dataclasses import dataclass, field
from typing import List


@dataclass
class Cargo:
    capacity: int
    contents: List[str] = field(default_factory=list)


@dataclass
class Vessel:
    name: str
    weapons: List[str] = field(default_factory=list)
    hold: Cargo
    hull_integrity = int
