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
    m = iinput()
    numbers = spt_map_int()
    numbers.sort()

    i = 0
    j = n - 1
    count = 0

    while i < j:
        sum = numbers[i] + numbers[j]
        if sum < m:
            i += 1
        elif sum > m:
            j -= 1
        else:
            count += 1
            i += 1
            j -= 1
    
    print(count)


sol()
