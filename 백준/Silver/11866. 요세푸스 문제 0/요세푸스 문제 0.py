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
    N, K = spt_map_int()
    d = deque(range(1, N+1))

    pmt = []
    while len(d) > 0:
        for _ in range(K - 1):
            d.append(d.popleft())
        pmt.append(d.popleft())

    print(f"<{', '.join(list(map(str, pmt)))}>")    


sol()
