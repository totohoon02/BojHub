import sys
from typing import *

input = sys.stdin.readline


def readline(sep=" ") -> List[str]:
    # read input as list of string
    return input().rstrip().split(sep)


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)


def map_to_int_list(str_list: List[str]) -> List[int]:
    return list(map(int, str_list))


class Solution:
    @staticmethod
    def solve():
        from collections import deque

        # 입력 처리
        n, m = map_to_int_list(readline())
        targets = map_to_int_list(readline())
        d = deque([x + 1 for x in range(n)])

        count = 0
        for target in targets:
            index = d.index(target)
            if index <= len(d) // 2:
                while index > 0:
                    d.append(d.popleft())
                    index -= 1
                    count += 1
            else:
                while index < len(d):
                    d.appendleft(d.pop())
                    index += 1
                    count += 1
            s = d.popleft()
        print(count)


Solution.solve()
