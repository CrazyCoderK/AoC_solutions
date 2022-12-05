import math
from aoc_utils import *
from aocd import get_data, submit
import copy
import string
import statistics

data = get_data(day=4,year=2022).splitlines()

def parse(data):
    for thingy in data:
        t = thingy.split(',')
        item = [t[0].split('-'),t[1].split('-')]
        for i in range(len(item)):
            item[i][0] = int(item[i][0])
            item[i][1] = int(item[i][1])
        data[data.index(thingy)] = item
    return data

data = parse(data)

def part_one(data):
    contained=0
    for item in data:
        if item[0][0] <= item[1][0] <= item[1][1] <= item[0][1]:
            contained+=1
        elif item[1][0] <= item[0][0] <= item[0][1]<= item[1][1]:
            contained+=1
    return contained

def part_two(data):
    overlap = 0
    for arr in data:
        if arr[0][0] <= arr[1][1] and arr[1][0] <= arr[0][1]:
            overlap += 1
    return overlap

print(f"Part 1: {part_one(data)}")
print(f"Part 2: {part_two(data)}")