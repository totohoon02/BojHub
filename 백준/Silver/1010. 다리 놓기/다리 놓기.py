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
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n - 1)

        def permutation(n, r):
            return factorial(n) // factorial(n - r)

        def combination(n, r):
            return permutation(n, r) // factorial(r)

        n = int(input())
        for _ in range(n):
            n, r = map_as_int_list(readline_as_str_list())
            if n < r:
                n, r = r, n

            print(combination(n, r))


Solution.solve()
