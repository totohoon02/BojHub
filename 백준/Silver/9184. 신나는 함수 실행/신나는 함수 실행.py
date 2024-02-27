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
        dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

        def w(a, b, c):
            if a <= 0 or b <= 0 or c <= 0:
                return 1

            if a > 20 or b > 20 or c > 20:
                return w(20, 20, 20)

            if dp[a][b][c]:
                return dp[a][b][c]
            elif a < b < c:
                dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
                return dp[a][b][c]
            else:
                dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
                return dp[a][b][c]

        while True:
            # 입력 처리
            a, b, c = map_to_int_list(readline_as_str_list())
            if a == b == c == -1:
                break

            # 출력
            print(f"w({a}, {b}, {c}) = {w(a, b, c)}")


sol = Solution()
sol.solve()
