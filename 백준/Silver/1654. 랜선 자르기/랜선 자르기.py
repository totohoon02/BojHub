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
    def get_max_length(self):
        k, n = map_to_int_list(readline_as_str_list())
        lines = [int(input()) for _ in range(k)]
        lines.sort()

        start = 1
        end = lines[-1]

        while start <= end:
            sum = 0

            mid = (start + end) // 2
            for line in lines:
                sum += line // mid

            if sum < n:
                end = mid - 1
            else:
                start = mid + 1

        print(end)


sol = Solution()
sol.get_max_length()
