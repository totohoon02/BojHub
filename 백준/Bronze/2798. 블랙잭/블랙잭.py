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
        n, m = map_as_int_list(readline_as_str_list())
        nums = map_as_int_list(readline_as_str_list())
        nums.sort(reverse=True)

        current_max = 0

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    current_sum = nums[i] + nums[j] + nums[k]
                    if current_sum == m:
                        print(current_sum)
                        return
                    else:
                        if current_max <= current_sum < m:
                            current_max = current_sum

        print(current_max)


Solution.solve()
