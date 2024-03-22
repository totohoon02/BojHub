import sys


def read_to_list() -> list:
    return list(map(int, sys.stdin.readline().split(" ")))


def dfs(start, visited: list) -> list:
    visited.append(start)

    for adj in sorted(graph[start]):
        if adj not in visited:
            dfs(adj, visited)
    return visited


def bfs(start) -> list:
    from collections import deque
    visited = [start]
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for adj in sorted(graph[node]):
            if adj not in visited:
                visited.append(adj)
                queue.append(adj)
    return visited


n, m, v = read_to_list()
graph = {x + 1: [] for x in range(n)}
for _ in range(m):
    n1, n2 = read_to_list()
    graph[n1].append(n2)
    graph[n2].append(n1)

d = dfs(v, [])
b = bfs(v)
print(" ".join(str(s) for s in d))
print(" ".join(str(s) for s in b))
