from data import male, female, lastnames
from typing import Dict
import random


def pick_name(lut):
    keys = tuple(lut.keys())
    key = random.choice(keys)
    name_data = lut[key]
    names, freqs = zip(*name_data)
    return random.choices(names, freqs)


def generate_name(lut: Dict):
    fname = pick_name(lut)
    mname = pick_name(lut)
    if lname is None:
        lname = pick_name(lastnames)
    return fname, mname, lname


def generate_gender():
    return random.choice("m", "f")
