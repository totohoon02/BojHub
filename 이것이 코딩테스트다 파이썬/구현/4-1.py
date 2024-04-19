import sys
from typing import *

input = sys.stdin.readline


def input_as_str_list(sep=" ") -> List[str]:
    return input().rstrip().split(sep)


def input_as_num_list(sep=" ") -> List[int]:
    return list(map(int, input_as_str_list(sep)))


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)


map_size = int(input())
moves = input_as_str_list()
cur = [1, 1]

for move in moves:
    if move == "U":
        if cur[0] - 1 > 0:
            cur[0] -= 1
    elif move == "D":
        if cur[0] + 1 < map_size:
            cur[0] += 1
    elif move == "L":
        if cur[1] - 1 > 0:
            cur[1] -= 1
    elif move == "R":
        if cur[1] + 1 < map_size:
            cur[1] += 1
print(cur)
