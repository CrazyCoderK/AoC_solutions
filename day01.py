import math
from aoc_utils import *
from aocd import get_data, submit
import copy
import string
import statistics

data = get_data(day=1, year=2022)

data = data.split("\n\n")
sums = list()
for a in data:
    sums.append(sum(map(lambda x: int(x), a.splitlines())))
#Answer 1
print(max(sums))
#Answer 2
print(sum(map(lambda x: int(x), sorted(sums, reverse=True)[:3])))