import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    from collections import deque
    n = iinput()
    d = deque([x + 1 for x in range(n)])

    while len(d) > 1:
        d.popleft()
        d.append(d.popleft())
    
    print(d.popleft())


sol()
