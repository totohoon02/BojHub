import sys
from typing import *

input = sys.stdin.readline


def input_as_str_list(sep=" ") -> List[str]:
    return input().rstrip().split(sep)


def input_as_num_list(sep=" ") -> List[int]:
    return list(map(int, input_as_str_list(sep)))


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)


pos = input() # a1
pos_num = [8 - ord('h') + ord(pos[0]), int(pos[1])]
moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], ]
count = 0

for move in moves:
    temp = [pos_num[0] + move[0], pos_num[1] + move[1]]
    if 0 < temp[0] < 9 and 0 < temp[1] < 9:
        count += 1
print(count)
