from data import male, female, lastnames
import random


def pick_name(lut):
    keys = tuple(lut.keys())
    key = random.choice(keys)
    name_data = lut[key]
    names, freqs = zip(*name_data)
    return random.choices(names, freqs)

def generate_name(lname=None):
    gender = random.choice("m", "f")
    lut = male if gender == "m" else female
    fname = pick_name(lut)
    mname = pick_name(lut)
    if lname is None:
        lname = pick_name(lastnames)
    return fname, mname, lname
    
    
    