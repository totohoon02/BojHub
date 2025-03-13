import sys
import string

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    # 60466175 36
    N, base = spt_map_int()
    rst = []
    chars = list(string.digits + string.ascii_uppercase)

    while N > 0:
        N, left = divmod(N, base)
        rst.append(chars[left])
    
    print("".join(rst)[::-1])

sol()

