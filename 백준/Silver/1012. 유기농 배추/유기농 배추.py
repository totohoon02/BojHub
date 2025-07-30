import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    n = iinput() # 케이스 수

    result = []
    # init condition
    for _ in range(n):
        width, height, num = spt_map_int() # 너비, 높이, 배추의 수
        area = [[0] * width for _ in range(height)]
        visited = [[False] * width for _ in range(height)]

        for _ in range(num):
            x, y = spt_map_int()
            area[y][x] = 1
        
        def dfs(y, x):
            visited[y][x] = True
            count = 1

            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0 <= ny < height and 0 <= nx < width:
                    if area[ny][nx] == 1 and not visited[ny][nx]:
                        count += dfs(ny, nx)

            return count

        
        temp = []

        for i in range(height):
            for j in range(width):
                if area[i][j] == 1 and not visited[i][j]:
                    temp.append(dfs(i,j))

        result.append(len(temp))
    
    for w in result:
        print(w)

sol()
