import sys
from typing import *

input = sys.stdin.readline


def readline_as_str_list(sep=" ") -> List[str]:
    return input().rstrip().split(sep)


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)


def map_to_int_list(str_list: List[str]) -> List[int]:
    return list(map(int, str_list))


class Solution:
    def solve(self):
        n = int(input())
        coordinates = [map_to_int_list(readline_as_str_list()) for _ in range(n)]
        coordinates.sort(key=lambda x: (x[1], x[0]))
        for coordinate in coordinates:
            print(join(list(map(str, coordinate)), " "))
sol = Solution()
sol.solve()
