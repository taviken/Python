from ._agent import Reputation, Agent, Name, Percent, Allegiance
import random
from typing import Optional
from _name_generator import male, female, pick_name, generate_gender


def make_agent(seed: Optional[int] = None):
    if seed is not None:
        random.seed(seed)
    gender = generate_gender()
    lut = male if gender == "m" else female
    fname = pick_name(lut)
    mname = pick_name(lut)
    lname = pick_name(lut)
    name = Name(fname, mname, lname)
    percent = Percent(random.random())
    Allegiance()
    agent = Agent(
        name,
        percent,
    )
