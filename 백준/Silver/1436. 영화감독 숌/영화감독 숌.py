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
        number = 666
        count = 1
        while count < n:
            number += 1
            if "666" in str(number):
                count += 1
        print(number)


Solution.solve()
