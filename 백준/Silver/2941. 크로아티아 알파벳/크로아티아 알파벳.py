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
    dup = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    
    for i in dup:
        sts = sts.replace(i, '*')

    print(len(sts))

sol()