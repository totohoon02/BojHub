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
    def get_cutter_height(self):
        # n: 나무 수, m: 가져갈 나무 길이
        n, m = map_to_int_list(readline_as_str_list())
        # 나무의 높이
        heights = map_to_int_list(readline_as_str_list())

        start = 1
        end = max(heights)
        mid = 0

        while start <= end:
            sum = 0

            mid = (start + end) // 2
            for h in heights:
                if h >= mid:
                    sum += h - mid

            if sum >= m:
                start = mid + 1
            else:
                end = mid - 1
        print(end)


sol = Solution()
sol.get_cutter_height()
