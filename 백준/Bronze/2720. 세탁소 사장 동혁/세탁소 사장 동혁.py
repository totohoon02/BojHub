import sys

input = sys.stdin.readline


def iinput():
    return int(input().strip())


def spt(sep=" "):
    return input().strip().split(sep)


def spt_map_int(sep=" "):
    return list(map(int, input().strip().split(sep)))


def sol():
    n = iinput()
    
    for _ in range(n):
        count = [0, 0, 0, 0]
        money = [25, 10, 5, 1]
        
        remain = iinput()

        for i in range(len(count)):
            count[i] = remain // money[i]
            remain = remain % money[i]

        print(" ".join(list(map(str, count))))

sol()
