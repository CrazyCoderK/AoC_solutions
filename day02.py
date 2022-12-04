import aoc_utils
import math
from aocd import get_data

with open("2022\input.txt") as f:
    data = f.read().splitlines()

choice = {"X":1, "Y":2, "Z":3}
outcomes = {"A X":3, "A Y":6, "A Z":0, "B X":0, "B Y":3, "B Z":6, "C X":6, "C Y":0, "C Z":3}
print("Part 1: ", sum(outcomes[x] + choice[x[-1]] for x in data))

strategy = {"A X":"A Z", "A Y":"A X", "A Z":"A Y", "B X":"B X", "B Y":"B Y", "B Z":"B Z", "C X":"C Y", "C Y":"C Z", "C Z":"C X"}

print("Part 2: ", sum(outcomes[x] + choice[x[-1]] for x in ( strategy[y] for y in data)))