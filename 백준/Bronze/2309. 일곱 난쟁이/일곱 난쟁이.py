import sys
from itertools import combinations


input = sys.stdin.readline

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

comb = combinations(dwarfs, 7)
for c in comb:
    if sum(c) == 100:
        for h in sorted(c):
            print(h)
        break