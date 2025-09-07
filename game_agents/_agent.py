from dataclasses import dataclass, field
from collections import namedtuple
from typing import List
from ._wugrb import WUBRG
from ._personal_attrs import PersonalAtrrs, Allegiance
from ._percent import Percent

Name = namedtuple("Name", ["first", "middle", "last"])


@dataclass
class Reputation:
    brutality: Percent  # lower is less lethal, higher is very lethal
    resolve: Percent  # how committed an agent is to what they do(ie if they say they're gonna kill, and don't - lower resolve)
    notable_encounters: List[str] = field(default_factory=list)


@dataclass
class Agent:
    name: Name
    loyalty: Percent
    alleigance: Allegiance
    reputation: Reputation
    personality: PersonalAtrrs
    monetary_goal: float
    allies: List["Agent"] = field(default_factory=list)
    alignment: WUBRG = WUBRG()
