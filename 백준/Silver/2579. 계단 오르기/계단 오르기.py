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


        # 입력 처리
        n = int(input())


        s = [int(input()) for _ in range(n)]

        # 예외 처리
        if n == 1 or n == 2:
            print(sum(s))
            return

        dp = [0] * n

        # 첫번째 까지 가는 경우 가중치 = 1
        dp[0] = s[0]

        # 두번째 까지 가는 경우 12 / 2
        dp[1] = max(s[0] + s[1], s[1])

        # 세번째 까지 가는 경우 13 / 23
        dp[2] = max(s[0] + s[2], s[1] + s[2])

        # END 에서 가능한 경우
        # END - 1 <== END - 3 (2는 연속)
        # END - 2
        for i in range(3, n):
            dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])

        print(dp[-1])

sol = Solution()
sol.solve()
