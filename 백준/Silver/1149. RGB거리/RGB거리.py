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
        cost = [map_to_int_list(readline_as_str_list()) for _ in range(n)]

        # 초기 값
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0] = cost[0]

        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

        print(min(dp[-1]))


sol = Solution()
sol.solve()
