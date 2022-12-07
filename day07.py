import math
from aoc_utils import *
from aocd import get_data, submit
import copy
import string
import statistics
import os
import re
import sys
from collections import defaultdict

data = get_data(day=7,year=2022).strip()
lines = [x for x in data.split('\n')]
print(lines)

dirs = defaultdict(int)
path = []
for line in lines:
    inp = line.strip().split()
    if inp[1] == 'cd':
        if inp[2] == '..':
            path.pop()
        else:
            path.append(inp[2])
    elif inp[1] == 'ls':
        continue
    elif inp[0] == 'dir':
        continue
    else:
        size = int(inp[0])
        # Add this file's size to the current directory size and the size of all parents
        for i in range(1, len(path)+1):
            dirs['/'.join(path[:i])] += size

maxUsage = 70000000 - 30000000
totalUsage = dirs['/']
needToFree = totalUsage - maxUsage

part1 = 0
part2 = 1e9
for _,val in dirs.items():
    # print(_,val)
    if val <= 100000:
        part1 += val
    if val>=needToFree:
        part2 = min(part2, val)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")