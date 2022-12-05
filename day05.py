import math
from aoc_utils import *
from aocd import get_data, submit
import copy
import string
import statistics

data = get_data(day=5,year=2022).splitlines()[10:]

# manually entered in the stacks
stack1 = list("DLVTMHF")
stack2 = list("HQGJCTNP")
stack3 = list("RSDMPH")
stack4 = list("LBVF")
stack5 = list("NHGLQ")
stack6 = list("WBDGRMP")
stack7 = list("GMNRCHLQ")
stack8 = list("CLW")
stack9 = list("RDLQJZMT")

original = {1:stack1,2:stack2,3:stack3,4:stack4,5:stack5,6:stack6,7:stack7,8:stack8,9:stack9}
stacks = copy.deepcopy(original)

for count, val in enumerate(data):
    val = val.split(" ")
    data[count] = [val[1],val[3],val[-1]]

# part 1
def move(stacks, data):
    for order in data:
        boxes = int(order[0])
        stackFrom = int(order[1])
        stackTo = int(order[2])
        for i in range(boxes):
            stacks[stackTo].append(stacks[stackFrom].pop(-1))
    return stacks

print("Part 1: ")
print("".join(stacks[i+1][-1] for i in range(9)))

# part 2
def move(stacks, data):
    for order in data:
        boxes = int(order[0])
        stackFrom = int(order[1])
        stackTo = int(order[2])
        moved = []
        for i in range(boxes):
            moved.append((stacks[stackFrom])[-1])
            stacks[stackFrom].pop(-1)
        moved.reverse()
        for j in moved:
            stacks[stackTo].append(j)
    return stacks

stacks = move(stacks, data)

print("Part 2: ")
print("".join(stacks[i+1][-1] for i in range(9)))
