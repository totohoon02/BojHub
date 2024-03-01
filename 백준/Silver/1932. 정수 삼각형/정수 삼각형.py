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
        values = [map_to_int_list(readline_as_str_list()) for _ in range(n)]

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, -1, -1):
                if i == n - 1:
                    dp[i][j] = values[i][j]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + values[i][j]
        print(dp[0][0])


sol = Solution()
sol.solve()
