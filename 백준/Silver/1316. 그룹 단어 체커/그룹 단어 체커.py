import sys

input = sys.stdin.readline

def spt():
    return input().split(" ")


def spt_map_int():
    return list(map(int, input().split(" ")))


def assertEqual(a, b):
    assert a == b


def sol():
    n = int(input())
    words = [input() for _ in range(n)]
    count = 0

    for w in words:
        s = set()
        last = ""
        if len(w) == 1:
            count += 1
            continue

        isGroup = True

        for c in w:
            if c != last and c in s:
                isGroup = False
                break
            s.add(c)
            last = c

        if isGroup:
            count += 1
            
    print(count)

sol()
