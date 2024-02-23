import sys
from typing import *

input = sys.stdin.readline


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)


def readline_as_str_list(sep=" ") -> List[str]:
    return input().split(sep)


def map_as_int_list(str_list: List[str]) -> List[int]:
    return list(map(int, str_list))


class Solution:
    @staticmethod
    def solve():
        from collections import deque
        # n : 총 인원수, k 건너 뛸 인덱스 수
        n, k = map_as_int_list(readline_as_str_list())

        ans = []
        d = deque([x + 1 for x in range(n)])
        while d:
            for _ in range(k - 1):
                d.append(d.popleft())
            ans.append(str(d.popleft()))

        print(f"<{join(ans, ', ')}>")


Solution.solve()
