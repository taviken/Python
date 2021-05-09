import multiprocessing
import time
import random


class WtfException(Exception):
    pass


def sleepy_function():
    num = random.random() * 10
    time.sleep(num)
    print(f'slept for {num} seconds')


def function_that_sometimes_fails():
    num = random.randint(0, 10)
    if num > 8:
        raise WtfException
    else:
        time.sleep(num)


def main1():
    multiprocessing.
