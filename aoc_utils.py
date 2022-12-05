import inspect
import os

def input_int_list():
    """parse input into a list of ints"""
    with open("AoC/input.txt", "r") as file:
        return [int(line.rstrip()) for line in file]


def input_string_list():
    """parse input into a list of strings"""
    with open("AoC/input.txt", "r") as file:
        return [line.rstrip() for line in file]


def input_block_list(data):
    arr, lis = [], []
    for count, val in enumerate(data):
        if val != "\n":
            lis.append(val)
        else:
            arr.append(lis)
            lis = []
    return arr

def filter_empty(li):
    """remove empty entries (e.g. when splitting a string)"""
    return list(filter(None, li))

def remove_comma_list(s):
    return [int(x) for x in s.split(",")]

def make_string_int(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l