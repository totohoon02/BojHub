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
        import heapq

        idx = 1
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        while True:
            # Get Input
            n = int(input())
            if n == 0:
                return

            # Init condition
            cave = [map_to_int_list(readline_as_str_list()) for _ in range(n)]
            visited = [[False] * n for _ in range(n)]
            q = []
            visited[0][0] = True
            heapq.heappush(q, (cave[0][0], 0, 0))  # cost, x, y

            while q:
                cost, x, y = heapq.heappop(q)

                # if reach to the end
                if x == n - 1 and y == n - 1:
                    print(f"Problem {idx}: {cost}")
                    idx += 1
                    break

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        heapq.heappush(q, (cost + cave[nx][ny], nx, ny))


sol = Solution()
sol.solve()
