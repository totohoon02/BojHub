import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    N, M = spt_map_int()
    trees = spt_map_int()

    start = 1
    end = max(trees)
    mid = 0

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for tree in trees:
            total += max(tree - mid, 0)
        
        if total >= M:
            start = mid + 1
        else:
            end = mid - 1
    
    print(end)

sol()
