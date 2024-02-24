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

    def get_max_budget(self):
        # 입력 처리
        n = int(input())
        asked = map_to_int_list(readline_as_str_list())
        asked.sort()
        total_budget = int(input())

        start = 1
        end = asked[-1]

        while start <= end:
            sum = 0

            #상한 값
            mid = (start + end) // 2

            for budget in asked:

                if budget <= mid:
                    sum += budget
                else:
                    sum += mid

            if sum <= total_budget:
                start = mid + 1
            else:
                end = mid - 1

        print(end)

sol = Solution()
sol.get_max_budget()
