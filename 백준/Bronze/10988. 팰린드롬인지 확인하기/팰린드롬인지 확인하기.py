import sys

input = sys.stdin.readline

def spt():
    return input().split(" ")


def spt_map_int():
    return list(map(int, input().split(" ")))


def assertEqual(a, b):
    assert a == b


def sol():
    sts = input().strip()
    print(1 if sts == sts[::-1] else 0)

sol()