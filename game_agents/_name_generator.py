from data import male, female
import random


def generate_name(gender):
    if gender == "m":
        keys = tuple(male.keys())
        lut = male
    else:
        keys = tuple(female.keys())
        lut = female
    key = random.choice(keys)
