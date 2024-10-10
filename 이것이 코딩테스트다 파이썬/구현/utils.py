import sys
from typing import *

input = sys.stdin.readline


def input_as_str_list(sep=" ") -> List[str]:
    return input().rstrip().split(sep)


def input_as_num_list() -> List[int]:
    return list(map(int, input_as_str_list()))


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)
