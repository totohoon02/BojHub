import sys
from typing import *

input = sys.stdin.readline


def input_as_str_list(sep=" ") -> List[str]:
    return input().rstrip().split(sep)


def input_as_num_list(sep=" ") -> List[int]:
    return list(map(int, input_as_str_list(sep)))


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)


n = int(input())
count = 0
for i in range(n + 1):
    for j in range(0, 60):
        for k in range(0, 60):
            time = join([str(i), str(j), str(k)])
            if "3" in time:
                count += 1
print(count)
