import sys
from typing import *

input = sys.stdin.readline


def input_as_str_list(sep=" ") -> List[str]:
    return input().rstrip().split(sep)


def input_as_num_list(sep=" ") -> List[int]:
    return list(map(int, input_as_str_list(sep)))


def join(str_list: List[str], sep="") -> str:
    return sep.join(str_list)


# 현재 방향을 기준으로 왼쪽부터 차례로 정한다.
# 갈 수 있으면 이동(바다가 아니고 가보지 않은 칸) 안되면 회전만
# 네방향 다 안되면 마지막 방향 유지 이전 위치로
# 이전도 바다면 정지 / 칸 수 출력

# Set Condition
n, m = input_as_num_list()
x, y, dir = input_as_num_list()  # 0 북쪽 1 동쪽 2 남쪽 3 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

wholeMap = []
visited = []
for i in range(n):
    wholeMap.append(input_as_num_list())
    visited.append([0] * m)

count = 1
turn_time = 0
visited[x][y] = 1

# move
while True:
    # Turn
    dir -= 1
    if dir < 0: dir = 3

    nx = x + dx[dir]
    ny = y + dy[dir]

    # 바다가 아니고 방문 안했다면!
    if wholeMap[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    # 네번 회전했을 때
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        # 이전 칸이 바다가 아니라면
        if wholeMap[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)
