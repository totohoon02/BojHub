import sys

input = sys.stdin.readline

def spt():
    return input().split(" ")


def spt_map_int():
    return list(map(int, input().split(" ")))


def assertEqual(a, b):
    assert a == b


def sol():
    ans = [1, 1, 2, 2, 2, 8]
    cur = spt_map_int()
    r = [ans[i] - cur[i] for i in range(len(ans))]
    print(" ".join(list(map(str, r))))

sol()
