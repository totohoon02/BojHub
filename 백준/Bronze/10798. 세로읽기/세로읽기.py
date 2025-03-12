import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    chars = [""] * 15
    
    for _ in range(5):
        sts = list(input().strip())
        for i in range(len(sts)):
            chars[i] += sts[i]
    print("".join(chars))


sol()
