import sys
from collections import Counter

input = sys.stdin.readline

counter = Counter()
n = int(input())

for _ in range(n):
    num = int(input())
    counter[num] += 1


for key in sorted(counter.keys()):
    for i in range(counter[key]):
        print(key)
