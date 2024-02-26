import sys
from typing import *

input = sys.stdin.readline


def readline_as_str_list(sep=" ") -> List[str]:
    return input().split(sep)


def map_as_int_list(str_list: List[str]) -> List[int]:
    return list(map(int, str_list))


class Solution:
    def lost_bracket(self):
        eq = input()
        nums = eq.split("-")

        ans = 0
        # first positive
        first = nums[0].split("+")
        for n in first:
            ans += int(n)

        #last negative
        for num_last in nums[1:]:
            last = num_last.split("+")
            for n in last:
                ans -= int(n)

        print(ans)

sol = Solution()
sol.lost_bracket()