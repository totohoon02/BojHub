import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    from itertools import permutations    
    _ = iinput()
    nums = spt_map_int()

    pers = permutations(nums, len(nums))

    max_num = 0
    for per in pers:
        cur = sum([abs(per[i] - per[i+1]) for i in range(0, len(per) - 1)])
        if cur > max_num:
            max_num = cur
    
    print(max_num)
    
sol()
