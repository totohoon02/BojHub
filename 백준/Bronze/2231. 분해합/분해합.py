import sys
from typing import *

input = sys.stdin.readline


def readline_as_str_list(sep=" ") -> List[str]:
    return input().split(sep)


def map_as_int_list(str_list: List[str]) -> List[int]:
    return list(map(int, str_list))


class Solution:
    @staticmethod
    def solve():
        n = int(input())
        scale = len(str(n))

        start_num = 0
        while True:
            str_num = str(start_num)
            gen = start_num + sum([int(x) for x in str_num])
            if n == gen:
                print(start_num)
                return
            start_num += 1

            if start_num > n:
                print(0)
                return

Solution.solve()
