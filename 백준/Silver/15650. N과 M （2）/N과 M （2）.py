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
        from itertools import combinations
        n, m = map_to_int_list(readline_as_str_list())
        for comb in combinations(range(1, n + 1), m):
            print(" ".join(list(map(str, comb))))


sol = Solution()
sol.solve()
