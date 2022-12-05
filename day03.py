import math
from aoc_utils import *
from aocd import get_data, submit
import copy
import string
import statistics

data = get_data(day=3,year=2022).strip().split("\n")

values = dict()
for index, lc in enumerate(string.ascii_lowercase):
  values[lc] = index + 1
for index, uc in enumerate(string.ascii_uppercase):
  values[uc] = index + 27

def part_one(data):
  priority_sum = 0
  for sack in data:
    first = set(sack[:len(sack)//2])
    second = set(sack[len(sack)//2:])
    for c in first:
      if c in second:
        priority_sum += values[c]
  return priority_sum

def part_two(data):
  priority_sum = 0
  while len(data) > 0:
    for c in set(data[0]):
      if (c in set(data[1]) and c in set(data[2])):
        priority_sum += values[c]
        break
    del data[:3]
  return(priority_sum)

print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")