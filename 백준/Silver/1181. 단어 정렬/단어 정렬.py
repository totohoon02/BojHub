import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
words = set()

for _ in range(n):
    word = input().strip()
    words.add(word)

words = list(words)
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)