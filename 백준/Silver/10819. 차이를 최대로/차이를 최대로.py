import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split(" ")))
pmts = permutations(nums, len(nums))

max_sum = 0
for pmt in pmts:
    cur_sum = 0
    for i in range(len(pmt) - 1):
        cur_sum += abs(pmt[i] - pmt[i+1])
        if cur_sum > max_sum:
            max_sum = cur_sum

print(max_sum)