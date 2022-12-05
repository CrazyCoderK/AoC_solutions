import math
from aoc_utils import *
from aocd import get_data, submit
import copy
import string
import statistics

data = get_data(day=2,year=2022).splitlines()

choice = {"X":1, "Y":2, "Z":3}
outcomes = {"A X":3, "A Y":6, "A Z":0, "B X":0, "B Y":3, "B Z":6, "C X":6, "C Y":0, "C Z":3}
print("Part 1:", sum(outcomes[x] + choice[x[-1]] for x in data))

strategy = {"A X":"A Z", "A Y":"A X", "A Z":"A Y", "B X":"B X", "B Y":"B Y", "B Z":"B Z", "C X":"C Y", "C Y":"C Z", "C Z":"C X"}

print("Part 2:", sum(outcomes[x] + choice[x[-1]] for x in ( strategy[y] for y in data)))