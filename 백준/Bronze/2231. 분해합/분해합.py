import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    n = iinput() # 216
    m = n
    min_gen = 0
    
    while m > 0:
        temp = m + sum(list(map(int, list(str(m)))))

        if temp == n:
            min_gen = m
            
        m -= 1

    print(min_gen)

sol()
