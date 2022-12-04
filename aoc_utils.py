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


def input_block_list():
    with open("AoC/input.txt") as f:
        data = f.read().splitlines()
    arr, lis = [], []
    for count, val in enumerate(data):
        if val != "":
            lis.append(val)
        else:
            arr.append(lis)
            lis = []
    return arr

def filter_empty(li):
    """remove empty entries (e.g. when splitting a string)"""
    return list(filter(None, li))