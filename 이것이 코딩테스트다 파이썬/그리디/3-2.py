import sys
from typing import *

input = sys.stdin.readline


def input_as_str_list(sep=" ") -> List[str]:
    return input().rstrip().split(sep)


def input_as_num_list() -> List[int]:
    return list(map(int, input_as_str_list()))


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)


n_num, iters, seq = input_as_num_list()
nums = input_as_num_list()
nums.sort(reverse=True)

result = 0
iter_count = 0
seq_count = 0

while iter_count < iters:
    if seq_count < seq:
        result += nums[0]
        seq_count += 1
    else:
        result += nums[1]
        seq_count = 0
    iter_count += 1

print(result)
