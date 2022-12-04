import math
from aoc_utils import *
from aocd import get_data, submit
from copy import deepcopy
import string

with open("2022\input.txt") as f:
    data = f.read().strip().split("\n")

values = dict()
for index, lc in enumerate(string.ascii_lowercase):
  values[lc] = index + 1
for index, uc in enumerate(string.ascii_uppercase):
  values[uc] = index + 27

def part_one():
  priority_sum = 0
  for sack in data:
    first = set(sack[:len(sack)//2])
    second = set(sack[len(sack)//2:])
    for c in first:
      if c in second:
        priority_sum += values[c]
  return priority_sum

def part_two():
  priority_sum = 0
  while len(data) > 0:
    for c in set(data[0]):
      if (c in set(data[1]) and c in set(data[2])):
        priority_sum += values[c]
        break
    del data[:3]
  return(priority_sum)

print(part_one())
print(part_two())