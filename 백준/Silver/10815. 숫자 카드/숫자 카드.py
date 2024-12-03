import sys

input = sys.stdin.readline


def spt():
    return input().split(" ")


def spt_map_int():
    return list(map(int, input().split(" ")))


n = int(input())
c1 = set(spt_map_int())
m = int(input())
c2 = spt_map_int()

pt = []

for c in c2:
    if c in c1:
        pt.append(1)
    else:
        pt.append(0)
print(" ".join(map(str, pt)))
