import sys
from collections import Counter
input = sys.stdin.readline


def spt():
    return list(map(int, input().split(" ")))


n = int(input())
cnt = Counter(spt())
m = int(input())
cards = spt()

count = []
for card in cards:
    if card in cnt.keys():
        count.append(cnt[card])
    else:
        count.append(0)

print(" ".join(list(map(str, count))))
