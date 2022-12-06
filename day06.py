import math
from aoc_utils import *
from aocd import get_data, submit
import copy
import string
import statistics

data = list(get_data(day=6,year=2022))

def find_marker(n, data):
    for i in range(len(data)-n+1):
        thing = [data[i:i+n]]
        if len(thing) == len(set(thing)):
                return i+n

print(f"Part 1: {find_marker(4, data)}")
print(f"Part 2: {find_marker(14, data)}")


